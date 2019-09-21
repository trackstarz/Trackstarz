from rest_framework import serializers
from universe.models import friendrequest

class friendrequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = friendrequest
        fields = '__all__'