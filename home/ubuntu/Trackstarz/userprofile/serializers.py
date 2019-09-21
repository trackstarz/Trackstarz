from rest_framework import serializers
from userprofile.models import userprofile

class userprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'