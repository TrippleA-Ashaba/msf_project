from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


@login_required
def index(request):
    todos = Todo.objects.filter(created_by=request.user).order_by("-created_at")
    context = {
        "todos": todos,
    }
    return render(request, "todo/index.html", context)


@login_required
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        if title:
            new_todo = Todo.objects.create(title=title, created_by=request.user)
            new_todo.save()
            return redirect("index")


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, created_by=request.user)
    if request.method == "DELETE":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, created_by=request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        if title and title != todo.title:
            todo.title = title
            todo.save()
        return redirect("index")
    context = {"todo": todo}
    return render(request, "todo/edit_todo.html", context)


@login_required
def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, created_by=request.user)
    if request.method == "POST":
        if not todo.completed:
            todo.completed = True
            todo.save()
        else:
            todo.completed = False
            todo.save()
        return redirect("index")
