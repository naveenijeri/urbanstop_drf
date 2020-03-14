from django.shortcuts import render
from .models import NoteModel
from .serializers import NoteModelSerializer
from rest_framework import generics
# Create your views here.

class NoteCreateAPIView(generics.CreateAPIView):
    queryset=NoteModel.objects.all()
    serializer_class=NoteModelSerializer

class NoteUpdateAPIView(generics.UpdateAPIView):
    queryset=NoteModel.objects.all()
    serializer_class=NoteModelSerializer
    lookup_field='id'

class NoteListAPIView(generics.ListAPIView):
    queryset =NoteModel.objects.all()
    serializer_class =NoteModelSerializer