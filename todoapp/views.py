from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.

@login_required
def home(request):
    user = request.user
    todos = Todo.objects.filter(author=user).order_by('-id')
    s = request.GET.get('s')
    if s:
        todos = todos.filter(title__icontains=s)
    t = request.GET.get('t')
    if t:
        todos = todos.filter(status__exact=t)
    ctx = {
        'todos': todos
    }
    return render(request, 'index.html', ctx)


@login_required
def single(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        commit = form.save(commit=False)
        commit.author = request.user
        commit.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)


@login_required
def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        t = form.save(commit=False)
        t.author = request.user
        t.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)


@login_required
def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('/')
