from rest_framework import serializers
from .models import Burst

class BurstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burst
        fields = ('id', 'author', 'title', 'bodytext', 'timestamp', 'picture', 'comment_count', 'view_count', 'overview', 'categories', 'trackstarz_article')