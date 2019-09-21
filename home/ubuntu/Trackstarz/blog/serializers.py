from rest_framework import serializers
from .models import Category, Burst, Comment, Reply, BurstLike, CommentLike, ReplyLike

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BurstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burst
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
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


