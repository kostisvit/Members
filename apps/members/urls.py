# urls.py
from django.urls import path
from .views import MemberListView, Export_data
from . import views

urlpatterns = [
    path('members', MemberListView.as_view(), name='members-list'),
    path('members/export', views.Export_data, name='members-list-export'),
]