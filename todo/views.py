from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.

def addTask(request):
    addTaskName = request.POST['task']
    Task.objects.create(task=addTaskName)
    return redirect('home')
