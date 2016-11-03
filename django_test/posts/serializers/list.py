from rest_framework import serializers

from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    author_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "url", "author_email")
