
from django.urls import path, include


urlpatterns = [path('', include('allauth.account.urls'))]

# for provider in providers.registry.get_list():
#     try:
#         prov_mod = importlib.import_module(provider.package + '.urls')
#     except ImportError:
#         continue
#     prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
#     if prov_urlpatterns:
#         urlpatterns += prov_urlpatterns
