from rest_framework import serializers
from .models import Category, Burst, Comment, Reply, BurstLike, CommentLike, ReplyLike
from userprofile.models import userprofile
from userprofile.serializers import userSerializer, userprofileSerializer
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BurstSerializer(serializers.ModelSerializer):
    author = userprofileSerializer(many=False)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Burst
        fields = ['id', 'author', 'title', 'bodytext', 'timestamp', 'picture', 'comment_count', 'view_count', 'overview', 'categories', 'trackstarz_article']


class CommentSerializer(serializers.ModelSerializer):
    burst = BurstSerializer()
    author = userprofileSerializer()
    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class BurstLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurstLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'


class ReplyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyLike
        fields = '__all__'


