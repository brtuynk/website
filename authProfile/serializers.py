from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from authProfile import models
from authProfile.models import UserProfile


class UserProfileCreateSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'username',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}, 'username': {'required': False}}

        def create(self, validated_data):
            username = validated_data.get('username')
            first_name = validated_data.get('first_name', "")
            last_name = validated_data.get('last_name', "")
            password = validated_data.get('password')

            user_obj = UserProfile(
                username=username,
                first_name=first_name,
                last_name=last_name
            )
            user_obj.set_password(password)
            user_obj.save()

            data = user_obj
            return data


class UserProfileListSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'first_name',
            'last_name',
            'username'
        )


#class HelloSerializer(serializers.Serializer):
#    """Serializers a name field for testing our APIView"""
#    name = serializers.CharField(max_length=10)


