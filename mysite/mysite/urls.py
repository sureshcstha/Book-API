"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import BookViewSet, FavoriteViewSet, FantasyViewSet, AdventureViewSet, RomanceViewSet, \
    MysteryViewSet, HorrorViewSet, ThrillerViewSet, ChildrenViewSet, MotivationalViewSet, HumorViewSet, PoetryViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('favorites', FavoriteViewSet)
router.register('fantasy', FantasyViewSet)
router.register('adventure', AdventureViewSet)
router.register('romance', RomanceViewSet)
router.register('mystery', MysteryViewSet)
router.register('horror', HorrorViewSet)
router.register('thriller', ThrillerViewSet)
router.register('children', ChildrenViewSet)
router.register('motivational', MotivationalViewSet)
router.register('humor', HumorViewSet)
router.register('poetry', PoetryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
