from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from . import forms

def index(request):
    tasks = Task.objects.all()[:10]
    context={
        'tasks':tasks
    }
    return render(request, 'index.html', context)

def details(request, id):
    task = Task.objects.get(id=id)
    context={
        'task':task
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        form = forms.AddTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            return redirect('/todo')
    else:
        form = forms.AddTask()
        return render(request, 'add.html', {'form':form})

def update(request):
    id = request.POST.get('task_id')
    if request.POST.get('finished'):
        val = 1
    else:
        val = 0
    print('val :' + str(val))
    task = Task.objects.filter(pk=id).update(finished=bool(val))
    return redirect('/todo')