from django.db import models
from django.utils import timezone

# Create your models here.

class NoteModel(models.Model):
    id=models.AutoField(primary_key=True)
    note_text=models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class UserModel(models.Model):
    notemodel=models.ForeignKey(NoteModel,on_delete=models.CASCADE,related_name='user_note',null=True,blank=True)
    username=models.CharField(max_length=50)