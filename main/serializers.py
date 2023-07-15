from rest_framework import serializers
from .models import ToDoList, Item

def getData (id) :
    model = ToDoList.objects.get(id=id)
    fields = "__all__"
    return model

class ToDoListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ToDoList
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Item
        fields = '__all__'

        

