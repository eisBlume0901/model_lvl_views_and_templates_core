from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('projects/', views.project_listing, name="project_listing"),
    path('project/new', views.create_project, name="create_project"),

    path('project/<slug:id>', views.project_detail, name="project_detail"),

]