from rest_framework import serializers
from fisher_man.models.user import User
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'user_type', 'name', 'place','mobile', 'password','latitude', 'longitude','created_at', 'is_active']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return User.objects.create(**validated_data)



class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type','name','place','mobile','latitude','longitude','is_active']

