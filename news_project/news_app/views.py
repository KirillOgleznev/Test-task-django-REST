from rest_framework import generics

from .models import NewsModel, TypeNewsModel
from .serializers import NewsModelSerializer, TypeNewsModelSerializer


class NewsModelAPIView(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class NewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class TypeNewsModelAPIView(generics.ListCreateAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer


class TypeNewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer
