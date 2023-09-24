from .serializers import TodoSerializer
from rest_framework import viewsets
from apps.todo.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
