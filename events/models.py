from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    EVENT_CHOICES = [
        ('1', 'First type'),
        ('2', 'Second type'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=EVENT_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text


class Respond(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text
