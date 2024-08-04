from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.project_listing, name="project_listing"),
    path('create_project/', views.create_project, name="create_project"),

    path('project_detail/', views.project_detail, name="project_detail"),
]