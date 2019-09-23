from rest_framework import serializers
from userprofile.models import userprofile
from django.contrib.auth.models import User

class userprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'