# views.py
from django.views.generic import ListView
from .models import Member

class MemberListView(ListView):
    model = Member
    template_name = 'app/member.html'  # Specify your template name
    context_object_name = 'members'
