from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . models import ToDoList, Item
from . forms import CreateNewList
from . serializers import ItemSerializer, ToDoListSerializer, getData


def delete_item (id, itemId) :
    toDoList = ToDoList.objects.get(id=id)
    toDel = toDoList.item_set.get(id=itemId)
    toDel.delete()

def view_lists (request) :
    toDoList = ToDoList.objects.all()
    tdlserializer = ToDoListSerializer(toDoList, many=True)
    return JsonResponse({"lists" : tdlserializer.data}, safe=False)

@api_view(["GET", "POST"])
def item_list (request, id) :
    if request.method == "GET" :
        items = ToDoList.objects.get(id=id).item_set.all()
        itemserializer = ItemSerializer(items, many=True)
        return JsonResponse({"lists" : itemserializer.data}, safe=False)

    if request.method == "POST" :
        itemserializer = ItemSerializer(data=request.data)
        if itemserializer.is_valid() :
            itemserializer.save()
            return Response(itemserializer.data, status=status.HTTP_201_CREATED)

def index(response, id):
    toDoList = ToDoList.objects.get(id=id)

    if response.method == "POST":

        if response.POST.get("save"):

            for item in toDoList.item_set.all():

                if response.POST.get("c" + str(item.id)):
                    item.complete = True
                else:
                    item.complete = False
                item.save()

                newItemName = response.POST.get("t" + str(item.id))
                if len(newItemName) < 2:
                    delete_item(id, int(item.id))
                else:
                    item.text = newItemName
                    item.save()                


        elif response.POST.get("newItem"):
            itemName = response.POST.get("new")
            if len(itemName) > 2:
                toDoList.item_set.create(text=itemName, complete=False, subtask=False)


    return render(response, "main/list.html", {"toDoList":toDoList})

def home (response) :
    toDoList = ToDoList.objects.all()

    print(f"Response: {response.POST.get('open')}")

    if response.method == "POST":
        print(f"POSTED!")
        for tdlist in toDoList:
            print(response.POST.get('open'))
            print(tdlist.id)
            if (str(response.POST.get('open')) == str(tdlist.id)):
                print(f"ID: {tdlist.id}")
                return HttpResponseRedirect("/%i" % tdlist.id)

    return render(response, "main/home.html", {"toDoList":toDoList})

def create (response) :
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if (form.is_valid()) :
            name = form.cleaned_data["name"]
            toDoList = ToDoList(name = name)
            toDoList.save()

            return HttpResponseRedirect("/%i" % toDoList.id)
    else :
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

    
