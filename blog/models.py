from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
#from django.db.models.signals import post_save



class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Burst(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, null=True, blank=True)
    bodytext = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)	
    picture = models.ImageField(upload_to='post_pics/%Y/%m/%d', blank=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    overview = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    trackstarz_article = models.BooleanField(default=False)
    
    
    def mytitle(self):
        return self.title
    
    def __unicode__(self):
        return self.bodytext
        
    def __str__(self):
        return self.bodytext[:60]

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def get_likers(self):
        return self.burstlikes.all().values_list('user', flat=True)



class Comment(models.Model):

    burst = models.ForeignKey(Burst, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp  = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.user.username

    @property
    def get_replies(self):
        return self.replies.all().order_by('timestamp')

    @property
    def get_likers(self):
        return self.commentlikes.all().values_list('user', flat=True)



class Reply(models.Model):

    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='reply_from_user', on_delete=models.CASCADE, null=True, blank=True)
    timestamp  = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.user.username

    @property
    def get_likers(self):
        return self.replylikes.all().values_list('user', flat=True)


class BurstLike(models.Model):

    user = models.ForeignKey(User, related_name='burstlikers', on_delete=models.CASCADE)
    burst = models.ForeignKey(Burst, related_name='burstlikes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CommentLike(models.Model):

    user = models.ForeignKey(User, related_name='commentlikers', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='commentlikes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ReplyLike(models.Model):

    user = models.ForeignKey(User, related_name='replylikers', on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, related_name='replylikes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username