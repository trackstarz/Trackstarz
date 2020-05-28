from rest_framework import serializers
from userprofile.models import userprofile

class userprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = ('id', 'user', 'displayname', 'startdate', 'coverphoto', 'about', 'youtube', 'twitter', 'instagram', 'pinterest', 'birthdate', 'website', 'picture', 'slug', 'friends')