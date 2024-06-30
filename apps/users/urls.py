from django.urls import path
from . import views
from .views import MemberUpdateView, CustomUserCreateView



urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('member/new/', CustomUserCreateView.as_view(), name='member_new' ),
    path('member/<int:pk>/edit/', MemberUpdateView.as_view(), name='member_edit'), #customuser(member)
]
