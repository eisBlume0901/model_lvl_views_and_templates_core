from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) # PROTECT means that if a user is deleted, the project will not be deleted

    def __str__(self):
        return self.name