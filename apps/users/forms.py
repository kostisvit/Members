from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from company.models import Company
from django.forms import ModelChoiceField


# Custom User New Form
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','first_name','last_name','date_joined')
        
        

# Custom User Change Form
class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control email-input', 'style': 'font-size: 16px;'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control first_name-input', 'style': 'font-size: 16px;'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff','phone_number')
    

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct email and password. Note that both fields may be case-sensitive."
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
    
    