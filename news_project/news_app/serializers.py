from rest_framework import serializers
from .models import NewsModel, TypeNewsModel


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"


class TypeNewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNewsModel
        fields = "__all__"
