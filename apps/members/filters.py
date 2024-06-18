import django_filters
from .models import Member

class MemberFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains',label="Επώνυμο")
    email = django_filters.CharFilter(lookup_expr='icontains',label="Email")
    phone_number = django_filters.CharFilter(lookup_expr='icontains',label="Τηλέφωνο")
    active = django_filters.ChoiceFilter(
        choices=[(True, 'Online'), (False, 'Offline')],
        empty_label='Any',
        label='Status'
    )
    class Meta:
        model = Member
        fields = {
            'city': ['icontains'],
            'email': ['icontains'],
            'phone_number': ['icontains'],
        }