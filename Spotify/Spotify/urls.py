from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from music.views import AlbumViewSet, QoshiqViewSet, QoshiqchiViewSet

router = DefaultRouter()
router.register('album', AlbumViewSet)
router.register('qoshiq', QoshiqViewSet)
router.register('qoshiqchi', QoshiqchiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
