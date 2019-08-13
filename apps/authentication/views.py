from .models import UserAuthentication
from django.shortcuts import render
from rest_framework import generics
from .serializer import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        user = request.data['user']
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
    'You have successfully signed up. Please now sign in',
    status=status.HTTP_201_CREATED
    )