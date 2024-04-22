"""
Views for the user API.
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from users.serializers import UserSerializer


class ListCreateUserView(generics.ListCreateAPIView):
    """View to create/list users"""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class DetailUserView(generics.RetrieveAPIView):
    """APIView to retrieve a user"""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class ManageProfileView(generics.RetrieveUpdateDestroyAPIView):
    """APIView to manage the authenticated user profile"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # ! Remember to add authentication_classes to the view

    def get_object(self):
        """Restricts users to manage only their own profile"""
        return self.request.user
