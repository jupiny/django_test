from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from posts.serializers import PostDetailSerializer
from posts.models import Post


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated,)
