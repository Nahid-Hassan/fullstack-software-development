from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    """
       * Used for read-write endpoints to represent a collection of model instances.
       * Provides get and post method handlers.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated, ) # can be tuple or list, include final comma

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
       * Used for read-write-delete endpoints to represent a single model instance.
       * Provides get, put, patch and delete method handlers.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated, ) # can be tuple of list, include final comma
    permission_classes = (IsAuthorOrReadOnly,)
      