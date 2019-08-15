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
