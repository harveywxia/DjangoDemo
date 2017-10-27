from django.contrib import auth
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    username = models.ForeignKey(auth.get_user_model())

