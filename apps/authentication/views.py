import jwt
from .models import UserAuthentication
from django.shortcuts import render
from rest_framework import generics
from .serializer import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from drugs import settings
# Create your views here.

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        user = request.data["user"]
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
    'You have successfully signed up. Please now sign in',
    status=status.HTTP_201_CREATED
    )

class LoginUserView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        email = request.data["user"]["email"]
        password = request.data["user"]["password"]
        if email is None or password is None:
            return Response(
                {
                    'error': 'Please provide both email and password to login'},
                status=status.HTTP_400_BAD_REQUEST)
        user = UserAuthentication.objects.filter(email=email ,password=password).first()
        if not user:
            return Response(
                {'error': 'Please enter valid credentials'}, status=status.HTTP_404_NOT_FOUND)
        pay_load = {
            'id': user.id,
            'username': user.username
        }
        token = jwt.encode(pay_load, settings.SECRET_KEY)
        return Response({"id": user.id, "username": user.username, "token": token}, status=status.HTTP_200_OK)