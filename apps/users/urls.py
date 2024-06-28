from django.urls import path
from . import views
from .views import MemberUpdateView



urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('member/<int:pk>/edit/', MemberUpdateView.as_view(), name='member_edit'), #customuser(member)
]
