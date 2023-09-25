from rest_framework import viewsets

from apps.todo.models import Todo

from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
