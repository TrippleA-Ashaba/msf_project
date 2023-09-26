from rest_framework import viewsets

from apps.todo.models import Todo

from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(created_by=self.request.user)
        else:
            return Todo.objects.none()
