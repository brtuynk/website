from django.db import models
#from django_resized import ResizedImageField
#from PIL import Image


class Test (models.Model):
    country = models.CharField(max_length=300, blank=True, null=True, unique=False, default='Common')
    language = models.CharField(max_length=300, blank=True, null=True, unique=False, default='English')
    description = models.CharField(max_length=3000, blank=False, null=False, unique=False, default='a')
    sub_name = models.CharField(max_length=300, blank=True, null=True, unique=False, default='')
    link = models.CharField(max_length=300, blank=True, null=True, unique=False, default='')
    #name_resize = ResizedImageField(size=[200, 200], quality=100, force_format='PNG',upload_to='image_projects', blank=True, null= True, unique = False, default = '')
    #image = ResizedImageField(size=[1200, 1200],quality=100,force_format='PNG', upload_to='image_projects', blank=True, null= True, unique = False, default = '')
