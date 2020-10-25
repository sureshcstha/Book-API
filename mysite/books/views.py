from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='favorites')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='adventure')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='thriller')
    serializer_class = BookSerializer


class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='children')
    serializer_class = BookSerializer


class MotivationalViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='motivational')
    serializer_class = BookSerializer


class HumorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='humor')
    serializer_class = BookSerializer


class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='poetry')
    serializer_class = BookSerializer
