from django.urls import path
from . import views
from .views import HomeView


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('', HomeView.as_view(), name='home')
    
]
