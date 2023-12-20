from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.owner = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    assigned_tasks = Task.objects.filter(assignee=request.user)
    context = {
        "assigned_tasks": assigned_tasks,
    }
    return render(request, "tasks/my_task.html", context)
