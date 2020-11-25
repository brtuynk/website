from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from authProfile.models import UserProfile
from authProfile.serializers import UserProfileCreateSerializer, UserProfileListSerializer


class UserProfileCreateAPIView(CreateAPIView):
    serializer_class = UserProfileCreateSerializer
    queryset = UserProfile.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer_user = UserProfileCreateSerializer(data=data)
        if serializer_user.is_valid(raise_exception=True):
            serializer_user.save()
            return Response(serializer_user.data, status=200)


class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()

