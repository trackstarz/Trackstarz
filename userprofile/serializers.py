from rest_framework import serializers
from userprofile.models import userprofile
from django.contrib.auth.models import User




class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class friendSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        depth = 1
        fields = ['id', 'user', 'displayname', 'startdate', 'coverphoto', 'about', 'youtube', 'twitter', 'instagram', 'pinterest', 'birthdate', 'website', 'picture', 'slug']

class userprofileSerializer(serializers.ModelSerializer):
    user = userSerializer(many=False)
    friends = friendSerializer(many=True)
    class Meta:
        model = userprofile
        fields = ['id', 'user', 'displayname', 'startdate', 'coverphoto', 'about', 'youtube', 'twitter', 'instagram', 'pinterest', 'birthdate', 'website', 'picture', 'slug', 'friends']