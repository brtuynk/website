from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authProfile import serializers
from authProfile.models import UserProfile
from authProfile.serializers import UserProfileCreateSerializer, UserProfileListSerializer, UserProfileUpdateSerializer


class UserProfileCreateAPIView(CreateAPIView):
    serializer_class = UserProfileCreateSerializer
    queryset = UserProfile.objects.all()

    """def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer_user = UserProfileCreateSerializer(data=data)
        if serializer_user.is_valid(raise_exception=True):
            serializer_user.save()
            return Response(serializer_user.data, status=200)"""


class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()


class UserProfileUpdateAPIView(UpdateAPIView):
    serializer_class = UserProfileUpdateSerializer
    queryset = UserProfile.objects.all()

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        self.update(request, *args, **kwargs)
        serializer = UserProfileUpdateSerializer(UserProfile.objects.filter(id=kwargs.get("pk")).first())
        return Response(serializer.data, status=200)


class UserProfileDeleteAPIView(DestroyAPIView):
    serializer_class = UserProfileCreateSerializer
    queryset = UserProfile.objects.all()





#class ApiView(APIView):
#    """Test API View"""
#    serializer_class = serializers.HelloSerializer
#
#    def get(self, request, format=None):
#
#        an_apiview = [
#            "Uses HTTP methods as function ",
#
#        ]
#
#        return Response({"message": "Hello", "an_apiview": an_apiview})
#
#    def post(self, request):
#        """Create a hello message with our name"""
#        serializer = self.serializer_class(data=request.data)
#
#        if serializer.is_valid():
#            name = serializer.validated_data.get("name")
#            message = f"Hello {name}"
#            return Response({"message": message})
#        else:
#            return Response(
#                serializer.errors,
#                status=status.HTTP_400_BAD_REQUEST
#            )
#
#    def put(self, request, pk=None):
#        """Handle updating an object"""
#        return Response({"method": "PUT"})
#
#    def patch(self, request, pk=None):
#        """Handle a partial update an object"""
#        return Response({"method": "PATCH"})
#
#    def delete(self, request, pk=None):
#        """Delete an object"""
#        return Response({"method": "DELETE"})


