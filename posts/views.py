from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, permissions
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer, UserSerializer

# Create your views here.

#normal view for listing and creating posts
"""class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAdminUser, )
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all() # get_user_model() is used to fetch the custom user model
    serializer_class = UserSerializer # Serializer for the User model

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer"""

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer