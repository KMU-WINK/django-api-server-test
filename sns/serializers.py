from rest_framework import serializers
from .models import Feed, Comment


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'owner')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'owner')