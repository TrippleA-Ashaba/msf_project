from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.todo.models import Todo

User = get_user_model()


class TodoViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )

        # Authenticate the client
        self.client.force_authenticate(user=self.user)

        # Create a sample todo
        self.todo_data = {
            "title": "Test Todo",
            "completed": False,
            "created_by": self.user,
        }
        self.todo = Todo.objects.create(**self.todo_data)

        self.todo_url = reverse("todo-list")

    def test_get_todo_list(self):
        response = self.client.get(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Todo")
        self.assertEqual(response.data[0]["completed"], False)

    def test_create_todo(self):
        new_todo_data = {
            "title": "New Todo",
            "completed": False,
            "created_by": self.user.id,
        }
        response = self.client.post(self.todo_url, new_todo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)

    def test_update_todo(self):
        updated_data = {
            "title": "Updated Todo",
            "completed": True,
            "created_by": self.user.id,
        }
        response = self.client.put(
            reverse("todo-detail", args=[self.todo.id]), updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated Todo")
        self.assertTrue(self.todo.completed)

    def test_delete_todo(self):
        response = self.client.delete(reverse("todo-detail", args=[self.todo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
