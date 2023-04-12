from django.contrib.auth.models import Group
from apps.accounts.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password', 'user_state']
    def validate_password(self, value):
        return make_password(value)
    
class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class passwordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only = True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only = True)
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Las contraseñas no coinciden'})
        return data