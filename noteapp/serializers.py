from .models import NoteModel,UserModel
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=('username',)

class NoteModelSerializer(serializers.ModelSerializer):
    user_note = UserModelSerializer(many=True)

    class Meta:
        model=NoteModel
        fields=('id','note_text','created_date','updated_date','user_note')

    def create(self, validated_data):
        user_data = validated_data.pop('user_note')
        note = NoteModel.objects.create(**validated_data)
        for user_data in user_data:
           UserModel.objects.create(notemodel=note, **user_data)
        return note

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user_note')
        users = (instance.user_note).all()
        users = list(users)
        instance.note_text = validated_data.get('note_text', instance.note_text)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.updated_date = validated_data.get('updated_date', instance.updated_date)
        instance.save()

        for user_data in user_data:
            user = users.pop(0)
            user.username = user_data.get('username', user.username)
           
            user.save()
        return instance


