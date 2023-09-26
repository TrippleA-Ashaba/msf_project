from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return render(request, "todo/home.html")


@login_required
def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todo/index.html", context)


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        if title:
            new_todo = Todo.objects.create(title=title, created_by=request.user)
            new_todo.save()
            return redirect("index")


def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    print("Here")
    if request.method == "DELETE":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        if title and title != todo.title:
            todo.title = title
            todo.save()
            return redirect("index")
