# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Member
from .filters import MemberFilter
from .export import Export_data

import logging
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
    filterset_class = MemberFilter
    paginate_by = 10


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