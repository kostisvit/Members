import django_filters
from .models import Member, Subscription

class MemberFilter(django_filters.FilterSet):
    membership_number = django_filters.CharFilter(lookup_expr='icontains',label="Κωδικός Μέλους")

    class Meta:
        model = Member
        fields = {
            'membership_number': ['icontains'],

        }


class SubscriptionFilter(django_filters.FilterSet):
    start_date = django_filters.NumberFilter(lookup_expr='year', label='Έτος')
    is_online = django_filters.ChoiceFilter(
        choices=[(True, 'Online'), (False, 'Offline')],
        empty_label='Any',
        label='Status'
    )
        
    class Meta:
        model = Subscription
        fields = ['start_date']
