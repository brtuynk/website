from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from test.models import Test
from rest_framework.serializers import ModelSerializer


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = [
            'id',
            "description",
            "sub_name",
            "link",
            "country",
            "language",
            #"name_resize",
            #"image",

        ]
        extra_kwargs = {"sub_name": {"required": False}, "link": {"required": False},
                        "name_resize": {"required": False}, "image": {"required": False}}


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = [
            "id",
            "description",
            "sub_name",
            "link",
            #"name_resize",
            #"image",
            'country',
            'language',

        ]
        extra_kwargs = {"sub_name": {"required": False}, "link": {"required": False},
                        "name_resize": {"required": False}, "image": {"required": False}}


class ProjectUpdateSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = [
            "id",
            "description",
            "sub_name",
            "link",
            "country",
            "language",
            #"name_resize",
            #"image",

        ]
        extra_kwargs = {"description": {"required": False},
                        "sub_name": {"required": False}, "link": {"required": False},
                        "name_resize": {"required": False}, "image": {"required": False}}
