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
    author = userprofileSerializer()
    class Meta:
        model = Comment
        depth = 0
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    author = userprofileSerializer()
    class Meta:
        model = Reply
        fields = '__all__'


class BurstLikeSerializer(serializers.ModelSerializer):
    author = userprofileSerializer()
    burst = BurstSerializer()
    class Meta:
        model = BurstLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    author = userprofileSerializer()
    comment = CommentSerializer()
    class Meta:
        model = CommentLike
        fields = '__all__'


class ReplyLikeSerializer(serializers.ModelSerializer):
    author = userprofileSerializer()
    reply = ReplySerializer()
    class Meta:
        model = ReplyLike
        fields = '__all__'


