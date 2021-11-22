from rest_framework import response
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
    
    def create(self, validated_data):
        psw = validated_data.get('password')
        username = validated_data.get('username')
        email = validated_data.get('email')

        user = User.objects.create(username=username, email=email)
        user.set_password(psw)
        user.save()
        return user

class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.pop('password', None)

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError(_('User not found'))
        user = User.objects.get(username=username)
        if user and user.check_password(password):
            refresh = self.get_token(user)
            validated_data['refresh'] = str(refresh)
            validated_data['access'] = str(refresh.access_token)
            return validated_data
        raise serializers.ValidationError("Email or password is incorrect")