from builtins import ValueError

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            "password": forms.PasswordInput
        }
    retype_password = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField(widget=forms.EmailInput)

    def clean_retype_password(self):
        password = self.cleaned_data['password']
        retype_password = self.cleaned_data['retype_password']
        if password != retype_password:
            raise ValidationError("The two password do not match")
        return retype_password

    def save(self, commit=True):
        new_user = super(RegisterForm, self).save(commit=False)
        new_user.set_password(self.cleaned_data['password'])
        if commit:
            new_user.save()
        return new_user