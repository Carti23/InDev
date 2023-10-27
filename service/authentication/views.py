from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Custom view for obtaining token pair
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)  # Allow any user to obtain tokens
    serializer_class = MyTokenObtainPairSerializer


# User registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # Allow any user to register
    serializer_class = RegisterSerializer


# Logout view for invalidating refresh tokens
class LogoutView(APIView):
    # Only authenticated users can log out
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()  # Blacklist the refresh token
            return Response({'message': 'You have been logged out successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
