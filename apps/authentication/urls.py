from django.urls import path
from .views import (SignUpView, LoginUserView)

urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('auth/login/', LoginUserView.as_view(), name='login')
]