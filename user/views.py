from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()