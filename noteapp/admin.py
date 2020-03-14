from django.contrib import admin
from .models import NoteModel,UserModel

# Register your models here.
admin.site.register(NoteModel)
admin.site.register(UserModel)

