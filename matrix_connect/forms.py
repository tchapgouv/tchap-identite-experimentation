from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')

    def confirm_login_allowed(self, user):
        pass