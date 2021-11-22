from rest_framework import generics
from django.contrib.auth import get_user_model

from todo.api.serializers import RegistrationSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer 

    def get_serializer_context(self):
        return {'request': self.request}

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    #Swagger
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)