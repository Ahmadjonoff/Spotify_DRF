from rest_framework.exceptions import APIException
from rest_framework.serializers import ModelSerializer
from .models import *

class QoshiqchiSer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbumSer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate_rasm(self, qiymat):
        if qiymat[-4:] == '.png' or qiymat[-4:] == '.jpg':
            return qiymat
        raise APIException("Noto`g`ri fayl!")

class QoshiqSer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_nom(self, qiymat):
        if qiymat[-4:] == '.mp3':
            return qiymat
        raise APIException("Qoshiq nomi '.mp3' bilan tugashi kerak")