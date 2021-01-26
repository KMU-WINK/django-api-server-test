from django.shortcuts import render
from .models import Feed, Comment
from .serializers import FeedSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions



class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        feed_id = self.kwargs["id"]
        queryset = Comment.objects.filter(feed_id=feed_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, feed_id=self.kwargs["id"])

