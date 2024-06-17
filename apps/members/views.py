# views.py
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Member
from .filters import MemberFilter

class MemberListView(FilterView):
    model = Member
    template_name = 'app/member.html'  # Specify your template name
    context_object_name = 'members'
    filterset_class = MemberFilter
    #paginate_by = 2
