from rest_framework.serializers import ModelSerializer

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


class UserProfileListSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

