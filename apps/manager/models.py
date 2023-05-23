from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):

    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.position})"

    def get_absolute_url(self):
        return reverse("manager:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    deadline = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)

    class PriorityChoices(models.TextChoices):
        URGENT = "U", _("Urgent")
        IMPORTANT = "I", _("Important")
        MINOR = "M", _("Minor")
        DEFERRED = "D", _("Deferred")

    priority = models.CharField(
        max_length=1,
        choices=PriorityChoices.choices,
        default=PriorityChoices.MINOR,
    )

    tasktype = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assigners = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return f"{self.name} with {self.priority} priority"
