# Courtesy of django-social-auth
import json

from django.core.exceptions import ValidationError
from django.db import models
try:
    from django.utils.encoding import smart_unicode as smart_text
except ImportError:
    from django.utils.encoding import smart_text


class JSONField(models.TextField):
    """Simple JSON field that stores python structures as JSON strings
    on database.
    """
    #__metaclass__ = models.SubfieldBase
    # TODO: should possibly add to_python method too

    # def __init__(self, *agrs, **kwargs):
    #
    # def from_db_value(self, value, expression, connection, context):


    def to_python(self, value):
        """
        Convert the input JSON value into python structures, raises
        django.core.exceptions.ValidationError if the data can't be converted.
        """
        if self.blank and not value:
            return None
        if isinstance(value, basestring):
            try:
                return json.loads(value)
            except Exception as e:
                raise ValidationError(str(e))
        else:
            return value

    def validate(self, value, model_instance):
        """Check value is a valid JSON string, raise ValidationError on
        error."""
        if isinstance(value, basestring):
            super(JSONField, self).validate(value, model_instance)
            try:
                json.loads(value)
            except Exception as e:
                raise ValidationError(str(e))

    def get_prep_value(self, value):
        """Convert value to JSON string before save"""
        try:
            return json.dumps(value)
        except Exception as e:
            raise ValidationError(str(e))

    def value_to_string(self, obj):
        """Return value from object converted to string properly"""
        return smart_text(self.get_prep_value(self._get_val_from_obj(obj)))

    def value_from_object(self, obj):
        """Return value dumped to string."""
        return self.get_prep_value(self._get_val_from_obj(obj))


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^allauth\.socialaccount\.fields\.JSONField"]) #TODO: check if this is fine to not use as South is deprecated
except:
    pass
