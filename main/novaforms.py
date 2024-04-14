# user_registration/forms.py

from django import forms # type: ignore
from .models import RegisterUser

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegisterUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email
