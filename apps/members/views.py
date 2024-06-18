# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Member
from .filters import MemberFilter
from .export import Export_data


# Member list view
class MemberListView(LoginRequiredMixin,FilterView):
    model = Member
    template_name = 'app/member.html'
    context_object_name = 'members'
    filterset_class = MemberFilter
    paginate_by = 10
