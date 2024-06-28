import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import EmailAuthenticationForm,CustomUserChangeForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import CustomUser
from django.views.generic.edit import UpdateView

# Configure logging
logger = logging.getLogger(__name__)

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


# Member update view
class MemberUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    #fields = '__all__'
    template_name = 'member_form.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')

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