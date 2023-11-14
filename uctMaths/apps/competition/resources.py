from __future__ import unicode_literals

from import_export import resources, fields

from .models import SchoolStudent, School, Invigilator, Venue


class SchoolStudentResource(resources.ModelResource):
    class Meta:
        model = SchoolStudent


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class InvigilatorResource(resources.ModelResource):
    #Custom fields for export.
    rt_name = fields.Field(attribute = 'rt_name', column_name='resp. teach. name')
    rt_phone_primary = fields.Field(attribute = 'rt_phone_primary', column_name='resp. teach. phone')
    rt_email = fields.Field(attribute = 'rt_email', column_name='resp. teach. email')
    school_name = fields.Field(attribute = 'school_name', column_name='school name')

    class Meta:
        model = Invigilator
        export_order = ('school_name', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'notes', 'venue',
                        'location', 'rt_name','rt_phone_primary','rt_email')


class VenueResource(resources.ModelResource):
    class Meta:
        model = Venue
