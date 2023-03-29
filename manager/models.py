from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:

        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIO_CHOICES = [("U", "Urgent"), ("H", "High"), ("M", "Medium"), ("L", "Low")]

    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIO_CHOICES, default="U")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="workers")

    class Meta:
        ordering = ["-deadline"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return (
            f"{self.name}"
            f" -> description: {self.description},"
            f" deadline: {self.deadline},"
            f" status: {self.is_completed},"
            f" priority: {self.get_priority_display()},"
            f" type: {self.task_type.name}"
        )


class Position(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="workers", null=True)

    class Meta:
        ordering = ["username"]
