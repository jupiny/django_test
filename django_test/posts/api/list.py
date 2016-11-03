from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from posts.serializers import PostListSerializer
from posts.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)
