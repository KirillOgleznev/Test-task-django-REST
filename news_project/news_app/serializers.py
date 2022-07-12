from rest_framework import serializers
from .models import NewsModel, TypeNewsModel


class TypeNewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNewsModel
        fields = '__all__'


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ('id', 'name', 'short_description', 'full_description', 'type')


class NewsReadModelSerializer(serializers.ModelSerializer):
    type = TypeNewsModelSerializer(read_only=True)

    class Meta:
        model = NewsModel
        fields = ('id', 'name', 'short_description', 'full_description', 'type')
        extra_kwargs = {
            'full_description': {'write_only': True},
        }
