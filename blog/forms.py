from blog.models import Burst
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class BurstForm(forms.ModelForm):
    bodytext = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Please enter the description'}))
    
    class Meta:
        model = Burst
        fields = ('bodytext', 'picture') 
        
