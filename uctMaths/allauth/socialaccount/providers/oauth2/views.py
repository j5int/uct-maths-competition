from datetime import timedelta

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from allauth.socialaccount.helpers import render_authentication_error
from allauth.socialaccount import providers
from allauth.socialaccount.providers.oauth2.client import (OAuth2Client,
                                                           OAuth2Error)
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialToken, SocialLogin

class OAuth2Adapter(object):
    expires_in_key = 'expires_in'
    supports_state = True

    def get_provider(self):
        return providers.registry.by_id(self.provider_id)

    def complete_login(self, request, app, access_token, **kwargs):
        """
        Returns a SocialLogin instance
        """
        raise NotImplementedError

    def parse_token(self, data):
        token = SocialToken(token=data['access_token'])
        token.token_secret = data.get('refresh_token', '')
        expires_in = data.get(self.expires_in_key, None)
        if expires_in:
            token.expires_at = timezone.now() + timedelta(seconds=int(expires_in))
        return token

class OAuth2View(object):
    @classmethod
    def adapter_view(cls, adapter):
        def view(request, *args, **kwargs):
            self = cls()
            self.request = request
            self.adapter = adapter()
            return self.dispatch(request, *args, **kwargs)
        return view

    def get_client(self, request, app):
        callback_url = reverse(self.adapter.provider_id + "_callback")
        callback_url = request.build_absolute_uri(callback_url)
        provider = self.adapter.get_provider()
        client = OAuth2Client(self.request, app.client_id, app.secret,
                              self.adapter.authorize_url,
                              self.adapter.access_token_url,
                              callback_url,
                              provider.get_scope(),
                              provider.get_auth_params())
        return client


class OAuth2LoginView(OAuth2View):
    def dispatch(self, request):
        app = self.adapter.get_provider().get_app(self.request)
        client = self.get_client(request, app)
        client.state = SocialLogin.stash_state(request)
        try:
            return HttpResponseRedirect(client.get_redirect_url())
        except OAuth2Error:
            return render_authentication_error(request)


class OAuth2CallbackView(OAuth2View):
    def dispatch(self, request):
        if 'error' in request.GET or not 'code' in request.GET:
            # TODO: Distinguish cancel from error
            return render_authentication_error(request)
        app = self.adapter.get_provider().get_app(self.request)
        client = self.get_client(request, app)
        try:
            access_token = client.get_access_token(request.GET['code'])
            token = self.adapter.parse_token(access_token)
            token.app = app
            login = self.adapter.complete_login(request,
                                                app,
                                                token,
                                                response=access_token)
            token.account = login.account
            login.token = token
            if self.adapter.supports_state:
                login.state = SocialLogin \
                    .verify_and_unstash_state(
                        request,
                        request.GET.get('state'))
            else:
                login.state = SocialLogin.unstash_state(request)
            return complete_social_login(request, login)
        except OAuth2Error:
            return render_authentication_error(request)

