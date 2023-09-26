from django.urls import path

from .views import home, index, add_todo, delete_todo

urlpatterns = [
    path("home/", home, name="home"),
    path("", index, name="index"),
    path("add_todo/", add_todo, name="add_todo"),
    path("delete_todo/<id>/", delete_todo, name="delete_todo"),
]
