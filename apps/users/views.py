from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import EmailAuthenticationForm
from django.contrib.auth import logout


# Login user function
def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  # Redirect to a success page.
    else:
        form = EmailAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout user function
def custom_logout(request):
    logout(request)
    return redirect('login')

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"
