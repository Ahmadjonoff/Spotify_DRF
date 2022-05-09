from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

class QoshiqchiViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSer

    @action(detail=True, methods=['GET'])
    def album(self, request, pk):
        q = Qoshiqchi.objects.get(id = pk)
        albums = q.albomlari.all()
        ser = AlbumSer(albums, many=True)
        return Response(ser.data)

class QoshiqViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSer

    def get_queryset(self):
        songs = Qoshiq.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            songs = Qoshiq.objects.annotate(
                similarity = TrigramSimilarity("nom", soz)
            ).filter(similarity__gte=0.1).order_by("-similarity")
        return songs

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Qoshiq.objects.all()
        qoshiq = get_object_or_404(queryset, pk=pk)
        qoshiq.eshitildi += 1
        qoshiq.save()
        ser = QoshiqSer(qoshiq)
        return Response(ser.data)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, ]
    ordering_fields = ['eshitildi', 'nom', 'davomiylik', 'yil']
    search_fields = ['id', 'nom', 'yil']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSer

    @action(detail=True, methods=['POST'])
    def qoshiq(self, request, pk):
        a = Album.objects.get(id = pk)
        qoshiq = request.data
        qoshiq['album'] = pk
        qoshiq = QoshiqSer(data=request.data)
        if qoshiq.is_valid():
            qoshiq.save()
            return Response(qoshiq.data, status=status.HTTP_201_CREATED)
        return Response(qoshiq.errors, status=status.HTTP_400_BAD_REQUEST)