from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name = "index"),
    path("home/", views.home, name = "home"),
    path("", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("lists/<int:id>", views.item_list, name = "items"),
    path("lists/", views.view_lists, name = "list"),
]