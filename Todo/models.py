from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_Created = models.DateTimeField(default = timezone.now)
    complete = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']