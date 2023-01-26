from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('possible', 'Possible'),
        ('random', 'Random'),
        ('impossible', 'Impossible'),
    )

    EVENT_CATEGORY_CHOICES = (
        ('info', 'Info'),
        ('attention', 'Attention'),
        ('alarm', 'Alarm'),
    )

    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    event_type = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=EVENT_CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='tags')
