from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Класс сериализатора пользователя """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    """ Класс сериализатора создания пользователя """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
