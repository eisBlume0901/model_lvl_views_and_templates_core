from django.db import models
from django.contrib.auth.models import *
from django.urls import reverse
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) # PROTECT means that if a user is deleted, the project will not be deleted

    class Meta: # You can easily add permissions to your model by using the Meta class
        # can_add_new_project is the codename of the permission
        # can add new project is the name of the permission
        permissions = [("can_add_new_project", "can add new project")] # look at the auth_permission table to see the permissions
    def get_absolute_url(self):
        return reverse("project:project_detail", args=[self.slug]) # This is the URL that will be used to redirect to the project detail page
    def __str__(self):
        return self.name