from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = (
    url(r'^createUser/', views.UserProfileCreateAPIView.as_view(), name="create User"),
    url(r'^listUser/', views.UserProfileListAPIView.as_view(), name="list User"),
    url(r'^updateUser/(?P<pk>[0-9_]+)/', views.UserProfileUpdateAPIView.as_view(), name="update User"),
    url(r'^deleteUser/(?P<pk>[0-9_]+)/', views.UserProfileDeleteAPIView.as_view(), name="delete User"),
    # path('apiview/', views.HelloApiView.as_view(), name="apiview"),

)
