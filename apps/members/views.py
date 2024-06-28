# views.py
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Member, Subscription
from .filters import SubscriptionFilter, MemberFilter
from .export import Export_data
from django.views.generic.edit import UpdateView

# Configure logging
logger = logging.getLogger(__name__)

# Member list view
class MemberListView(LoginRequiredMixin,FilterView):
    model = Member
    template_name = 'app/member.html'
    context_object_name = 'members'
    filterset_class = MemberFilter
    paginate_by = 10
    
    def get_queryset(self):
        return Member.objects.filter(company=self.request.user.company)


# Subscription list 
class SubscriptionListView(LoginRequiredMixin, FilterView):
    model = Subscription
    #fields = '__all__'
    filterset_class = SubscriptionFilter
    template_name = 'app/subscription.html'
    context_object_name = 'subscriptions'
    paginate_by = 10
    
    def get_queryset(self):
        return Subscription.objects.filter(member__company=self.request.user.company)
