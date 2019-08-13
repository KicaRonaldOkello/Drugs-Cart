from rest_framework import serializers
from .models import UserAuthentication

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthentication
        fields = [
            'first_name', 'last_name', 'email', 'location', 'mobile_number',
            'is_staff', 'date_joined', 'username', 'password'
            ]