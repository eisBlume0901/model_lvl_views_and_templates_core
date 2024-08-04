from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import Projectform, AuthenticatedUserForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def project_listing(request):
    project_data = Project.objects.all()
    context = {
        "project_data": project_data
    }
    return render(request, "project.html", context)

def create_project(request):
    form = Projectform()

    return render(request, "create_project.html", {"form": form})

def project_detail(request):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_detail": project
    }
    return render(request, "detail.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticatedUserForm(data=request.POST)
        if form.is_valid():
            return redirect("index")
    else:
        form = AuthenticatedUserForm()
    return render(request, "login.html", {"form": form})
