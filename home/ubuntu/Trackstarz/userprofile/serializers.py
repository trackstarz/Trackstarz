from rest_framework import serializers
from userprofile.models import userprofile
from django.contrib.auth.models import User




class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class userprofileSerializer(serializers.ModelSerializer):
    user = userSerializer(many=False)
    class Meta:
        model = userprofile
        fields = ['id', 'user', 'displayname', 'startdate', 'coverphoto', 'about', 'youtube', 'twitter', 'instagram', 'pinterest', 'birthdate', 'website', 'picture', 'slug', 'friends']