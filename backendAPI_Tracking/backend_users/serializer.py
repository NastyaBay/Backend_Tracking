from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import CustomUser

# Вывод списка пользователей
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')


# Регистрация и авторизация
class UserCreateSerializer(UserCreateSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return super().create(validated_data)