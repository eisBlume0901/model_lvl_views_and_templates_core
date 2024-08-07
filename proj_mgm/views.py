from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import Projectform, AuthenticatedUserForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")
@login_required(login_url="/login/")
@permission_required("proj_mgm.view_project")
def project_listing(request):
    project_data = Project.objects.all()
    context = {
        "project_data": project_data
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
@permission_required("proj_mgm.view_project")
def project_detail(request, id):
    project = get_object_or_404(Project, slug=id)
    context = {
        "project_detail": project
    }
    return render(request, "detail.html", context)


@login_required(login_url="/login/")
@permission_required(
    {("proj_mgm.view_project"), ("proj_mgm.can_add_new_project")}
)
def create_project(request):
    form = Projectform()
    if request.method == "POST":
        form = Projectform(data=request.POST)
        if form.is_valid():
            project = form.save(commit=False) # commit set to false means that the object is not saved to the database
            # We have to do the commit set to false first because we need to add the user to the project
            project.user = request.user
            project.save()
            messages.success(request, "Project created successfully")
            return redirect("project_listing")
        else:
            messages.error(request, "Project creation failed. Please try again")

    return render(request, "create_project.html", {"form": form})


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