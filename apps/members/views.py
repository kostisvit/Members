# views.py
from django.views.generic import ListView
from .models import Member

class MemberListView(ListView):
    model = Member
    template_name = 'home.html'  # Specify your template name
    context_object_name = 'members'
