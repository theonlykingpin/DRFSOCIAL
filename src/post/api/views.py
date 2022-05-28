from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.api.serializers import PostListSerializer
from post.models import Post


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
