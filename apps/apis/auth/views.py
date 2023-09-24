from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

import secrets
import string


def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


User = get_user_model()


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response(
                {
                    "token": token.key,  # Return the token key
                    "message": "Login successful!",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutAPIView(APIView):
    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)


class PasswordChangeAPIView(APIView):
    def post(self, request):
        user = request.user
        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")

        if not user.check_password(current_password):
            return Response(
                {"error": "Invalid current password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()

        request.auth.delete()

        return Response(
            {"message": "Password changed successfully"}, status=status.HTTP_200_OK
        )


class ResetPasswordAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
            # Generate a random password
            new_password = generate_random_password()

            # Set the new password for the user
            user.set_password(new_password)
            user.save()

            request.auth.delete()

            # Print out the new password (for testing purposes)
            print(f"New Password for {user.get_full_name()}: {new_password}")

            return Response(
                {"message": "Password reset successfully"}, status=status.HTTP_200_OK
            )

        except User.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
