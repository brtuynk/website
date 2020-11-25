from django.conf.urls import url
from . import views

urlpatterns = [
    url('createUser/', views.UserProfileCreateAPIView.as_view(), name="create User"),
    url('listUser/', views.UserProfileListAPIView.as_view(), name="list User"),

]