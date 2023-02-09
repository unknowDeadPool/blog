from rest_framework import generics
from applications.post.models import Post
from applications.post.serializers import PostSerializer

# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateAPIView(generics.CreateAPIView):
#     serializer_class = PostSerializer

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     look_field = 'id'

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer