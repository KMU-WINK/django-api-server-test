from django.shortcuts import render
from .models import Feed, Comment
from .serializers import FeedSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


class IsMe(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":  # GET을 제외한 모든 메서드는 대상이 소유자를 구분함
            return True
        else:
            return obj == request.user


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsMe]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsMe]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

