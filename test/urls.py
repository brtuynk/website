from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from test import views

router = DefaultRouter()
router.register('viewset', views.TestViewSet)


urlpatterns = [
    #url(r'^createProject/', views.ProjectCreateAPIView.as_view(), name="create Project"),
    #url(r'^updateProject/(?P<pk>[0-9_]+)', views.ProjectUpdateAPIView.as_view(), name="update Project"),
    #url(r'^deleteProject/(?P<pk>[0-9_]+)', views.ProjectDeleteAPIView.as_view(), name="delete Project"),
    #
    #path("listProject/all/", views.ProjectListAllAPIView.as_view(), name="list Project"),
    #path("listProject/", views.ProjectList_EN_APIView.as_view(), name="list Project"),
    #path("listProject/tr/", views.ProjectList_TR_APIView.as_view(), name="list Project"),
    #path("listProject/UK/en/", views.ProjectList_UK_EN_APIView.as_view(), name="list Project"),
    #path("listProject/UK/tr/", views.ProjectList_UK_TR_APIView.as_view(), name="list Project"),

    path("", include(router.urls))
]
