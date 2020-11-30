from rest_framework import viewsets

from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


from test.models import Test
from test.serializers import TestSerializer, ProjectListSerializer, ProjectUpdateSerializer

from django.db.models import Q


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

#    def create(self, request):
#        serializer = self.serializer_class(data=request.data)
#
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            test_return = serializer.data
#            return Response(test_return, status=200)
#


#    def perform_create(self, serializer):
#        serializer.save()


    #def post(self, request, *args, **kwargs):
    #    #check_if_admin(request)
    #    data = request.data.copy()
    #    serializer_project = ProjectCreateSerializer(data=data)
    #    if serializer_project.is_valid(
    #            raise_exception=True):  # raise_exception hatanın ne oldugunu formatının nasıl olması gerektiğini söylüyor
    #        serializer_project.save()
    #        project_return = serializer_project.data
    #        return Response(project_return, status=200)


class ProjectListAllAPIView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = Test.objects.all()


class ProjectList_EN_APIView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = Test.objects.filter((Q(country="TR")|Q(country="Common")) & Q(language="English"))


class ProjectList_TR_APIView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = Test.objects.filter((Q(country="TR")|Q(country="Common")) & Q(language="Turkish"))


class ProjectList_UK_EN_APIView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = Test.objects.filter((Q(country="UK")|Q(country="Common")) & Q(language="English"))


class ProjectList_UK_TR_APIView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = Test.objects.filter((Q(country="UK")|Q(country="Common")) & Q(language="Turkish"))


class ProjectUpdateAPIView(UpdateAPIView):
    serializer_class = ProjectUpdateSerializer
    queryset = Test.objects.all()

    def put(self, request, *args, **kwargs):
        #check_if_admin(request)
        kwargs['partial'] = True
        self.update(request, *args, **kwargs)
        serializer = ProjectUpdateSerializer(Test.objects.filter(id=kwargs.get("pk")).first())
        return Response(serializer.data, status=200)


    """
    def put(self, request, *args, **kwargs):
        check_if_admin(request)
        data = request.data.copy()
        serializer_project = ProjectUpdateSerializer(data=data)
        if serializer_project.is_valid():
            serializer_project.save()
            project_return = serializer_project.data
            return Response(project_return, status=200)
        else:
            raise ValidationError('Wrong data format')
    """


class ProjectDeleteAPIView(DestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def destroy(self, request, *args, **kwargs):
        #check_if_admin(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response('deleted', status=200)
