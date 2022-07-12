from rest_framework import generics

from .models import NewsModel, TypeNewsModel
from .serializers import NewsModelSerializer, TypeNewsModelSerializer


class NewsModelAPIView(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer

    # def list(self, request, *args, **kwargs):
    #     objects = NewsModel.objects.get(username="moeedlodhi")
    #     serialized = self.get_serializer(objects)
    #     print('listing a model here')
    #     return Response({"data": serialized.data})


class NewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class TypeNewsModelAPIView(generics.ListCreateAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer


class TypeNewsModelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeNewsModel.objects.all()
    serializer_class = TypeNewsModelSerializer
