from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
#from django.db.models.signals import post_save
from django.utils.text import slugify



class userprofile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=40)
    startdate = models.DateField(default = timezone.now)
    coverphoto = models.ImageField(upload_to='cover_images/%Y/%m/%d', blank=True, default='cover_images/2019/08/13/New-Logo-Youtube-2.png')
    about = models.TextField(null=True, blank=True)
    youtube = models.URLField(max_length = 200, null=True, blank=True)
    twitter = models.URLField(max_length = 200, null=True, blank=True)
    instagram = models.URLField(max_length = 200, null=True, blank=True)
    pinterest = models.URLField(max_length = 200, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images/%Y/%m/%d', blank=True, default='profile_images/2019/08/13/New-Trackstarz-App-logo.png')
    slug = models.SlugField()
    friends = models.ManyToManyField("userprofile", blank=True)
    
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def save(self, *args,  **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        super(userprofile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/universe/{}".format(self.slug)
        





