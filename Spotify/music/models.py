import datetime

from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    davlat = models.CharField(max_length=30)
    yonalish = models.CharField(max_length=20)

    def __str__(self):
        return self.ism

class Album(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.URLField(blank=True)
    yil = models.DateField()
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE, related_name='albomlari')

    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=30)
    yil = models.DateField()
    matn = models.CharField(max_length=300, blank=True)
    davomiylik = models.DurationField(default=datetime.timedelta(seconds=210), blank=True)
    qoshiq = models.URLField(blank=True)
    eshitildi = models.PositiveIntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='qoshiqlari')

    def __str__(self):
        return self.nom