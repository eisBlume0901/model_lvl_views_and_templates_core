from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import Projectform, AuthenticatedUserForm
# Create your views here.
def index(request):
    return render(request, "index.html")

@permission_required("proj_mgm.view_project", login_url="login")
def project_listing(request):
    project_data = Project.objects.all()
    context = {
        "project_data": project_data
    }
    return render(request, "project.html", context)

def create_project(request):
    form = Projectform()

    return render(request, "create_project.html", {"form": form})

@login_required(login_url="login")
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
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
    else:
        form = AuthenticatedUserForm()
    return render(request, "login.html", {"form": form})

def logout(request): # Needs logout for debugging to ensure that permissions are working
    auth_logout(request)
    return redirect("index")