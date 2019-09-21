from userprofile.models import userprofile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password' )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ('picture', 'displayname', 'coverphoto')