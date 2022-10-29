from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def todo_list(request):
    Todos = Todo.objects.all()
    context = {
        'todos': Todos
    }

    return render(request, 'todo/todo_list.html', context)

@login_required(login_url='accounts:login')
def todo_create(request):
    form = TodoForm()
    context = {
        'form': form
    }
    if request.method  == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/created')

    return render(request, 'todo/todo_create.html', context)

def todo_created(request):
    return render(request, 'todo/todo_created.html')


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return render(request, 'todo/todo_deleted.html' )

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/todo_updated')
    context = {'form': form}
    return render(request, 'todo/todo_update.html', context)


def todo_updated(request):
    return render(request, 'todo/todo_updated.html')