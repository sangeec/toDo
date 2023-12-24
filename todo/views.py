from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.


def addTask(request):
    addTaskName = request.POST['task']
    Task.objects.create(task=addTaskName)
    return redirect('home')


def mark_as_done(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, taskId):
    task_name = get_object_or_404(Task, pk=taskId)
    if request.method == 'POST':
        new_task_name = request.POST['task']
        task_name.task = new_task_name
        task_name.save()
        return redirect('home')
    else:
        context = {
            'get_task_name': task_name
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    task.delete()
    return redirect('home')