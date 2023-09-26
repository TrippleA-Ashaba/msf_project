from django.urls import path

from .views import add_todo, complete_todo, delete_todo, edit_todo, index

urlpatterns = [
    path("", index, name="index"),
    path("add_todo/", add_todo, name="add_todo"),
    path("delete_todo/<id>/", delete_todo, name="delete_todo"),
    path("edit_todo/<id>/", edit_todo, name="edit_todo"),
    path("complete_todo/<id>/", complete_todo, name="complete_todo"),
]
