from import_export import resources, fields
from .models import Member

class MemberResource(resources.ModelResource):
    first_name = fields.Field(attribute="first_name",column_name="Όνομα",)
    last_name = fields.Field(attribute="last_name",column_name="Επώνυμο",)
    date_of_birth = fields.Field(attribute="date_of_birth",column_name="Ημ.Γένν.",)

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'date_of_birth','email', 'phone_number', 'address','city','postal_code','country','gender', 'membership_date','active','company')
        export_order = ('first_name', 'last_name', 'date_of_birth','email', 'phone_number', 'address','city','postal_code','country','gender', 'membership_date','active','company')
        widgets = {
            'date_of_birth': {'format': '%d/%m/%Y'},
            'membership_date': {'format': '%d/%m/%Y'},
        }