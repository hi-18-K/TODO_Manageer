from django.shortcuts import render, redirect , get_object_or_404 , reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):              #display todo page
    #todo_list = Todo.objects.order_by('id')
    user = request.user
    todo_list_one = Todo.objects.all()
    todo_list = []
    for td in todo_list_one:
        if td.author.id == user.id:
            todo_list.insert(0,td)
    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@require_POST                   #add task to todo
def addTodo(request):
    form = TodoForm(request.POST)
    user = request.user
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'] ,
                        priority=request.POST['priority'],
                        type=request.POST['type'],
                        duedate=request.POST['duedate'],
                        author=user)
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id): #mark completed task from todo
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):   #delete compelted task
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):         #delete all tasks
    Todo.objects.all().delete()

    return redirect('index')
