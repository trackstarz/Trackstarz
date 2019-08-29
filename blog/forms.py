from blog.models import Burst, Comment, Reply, BurstLike, CommentLike, ReplyLike
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
        


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'comment_input',
        'placehoder': 'Type your comment',
        'rows': '1',
        'maxlength': '500'
    }))
    class Meta:
        model = Comment
        fields = ('content', 'burst' )


class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'comment_input',
        'placehoder': 'Type your reply',
        'rows': '1',
        'maxlength': '500'
    }))
    class Meta:
        model = Reply
        fields = ('content', 'comment', 'from_user' )


class BurstLikeForm(forms.ModelForm):
    class Meta:
        model = BurstLike
        fields = ('burst',)


class CommentLikeForm(forms.ModelForm):
    class Meta:
        model = CommentLike
        fields = ('comment',)


class ReplyLikeForm(forms.ModelForm):
    class Meta:
        model = ReplyLike
        fields = ('reply',)
