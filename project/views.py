from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project import serializers, models


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectCreateSerializer
    queryset = models.Project.objects.all()

    def perform_create(self, serializer):
        serializer.save() # parantezin içine first_name(modelin içinde verilen herhangi bir field olabilir)=self.request.user yazılırsa create eden user'ın adı otomatik gelir.


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update",
            """Automatically maps to URLs using Routers""",
            """Provides more functionality with less code"""
        ]

        return Response({"message": "hello", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
