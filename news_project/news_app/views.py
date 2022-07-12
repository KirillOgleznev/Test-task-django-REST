from rest_framework import generics

from .models import NewsModel, TypeNewsModel
from .serializers import NewsModelSerializer, TypeNewsModelSerializer, NewsReadModelSerializer


class NewsModelAPIView(generics.ListCreateAPIView):
    serializer_class = NewsModelSerializer

    def get_serializer_class(self):
        if self.request.method in ('GET',):
            return NewsReadModelSerializer
        return NewsModelSerializer

    def get_queryset(self):
        queryset = NewsModel.objects.all()
        type_news = self.request.query_params.get('id')
        if type_news is not None:
            queryset = queryset.filter(type=type_news)
        return queryset


class NewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class TypeNewsModelAPIView(generics.ListCreateAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer


class TypeNewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer
