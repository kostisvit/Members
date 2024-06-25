# views.py
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Member
#from .filters import MemberFilter,SubscriptionFilter
from .export import Export_data
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

# Configure logging
logger = logging.getLogger(__name__)

# Member list view
class MemberListView(LoginRequiredMixin,FilterView):
    model = Member
    template_name = 'app/member.html'
    context_object_name = 'members'
    #filterset_class = MemberFilter
    paginate_by = 10
    
    # def get_queryset(self):
    #     return Member.objects.filter(user=self.request.user)

# Member Profile Update
class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'
    template_name = 'member_form.html'
    success_url = reverse_lazy('home')  # Assuming you have a book list view

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            logger.info(f'Member "{self.object}" updated successfully.')
            messages.success(self.request, 'Book updated successfully.')
            return response
        except Exception as e:
            logger.error(f'Error updating book: {e}')
            form.add_error(None, 'An error occurred while updating the book.')
            return super().form_invalid(form)



# Subscription list 
# class SubscriptionListView(LoginRequiredMixin, FilterView):
#     model = Subscription
#     #fields = '__all__'
#     filterset_class = SubscriptionFilter
#     template_name = 'app/subscription.html'
#     context_object_name = 'subscriptions'
#     paginate_by = 10
    
#     def get_queryset(self):
#         return Subscription.objects.filter(member__user=self.request.user)
