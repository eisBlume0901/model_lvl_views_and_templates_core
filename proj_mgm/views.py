from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def project_listing(request):
    return render(request, "project.html")

def create_project(request):
    return render(request, "create_project.html")

def project_detail(request):
    return render(request, "detail.html")

