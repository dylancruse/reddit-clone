from rest_framework import serializers

from .models import Post, Comment


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'created_by')