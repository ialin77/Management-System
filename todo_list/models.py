import uuid

from django.db import models

from projects.models import Project
from account.models import User


class TodoList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    project = models.ForeignKey(Project, related_name='todo_lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='todo_lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name