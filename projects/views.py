from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/project_list.html", context)

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.tasks.all()
    context = {
        "project": project,
        "tasks": tasks,
    }
    return render(request, "projects/detail.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_project.html", context)
