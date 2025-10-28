# snippets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'snippets/register.html', {'form': form})


def snippet_list(request):
    snippets = Snippet.objects.filter(public=True).order_by('-created_at')
    return render(request, 'snippets/snippet_list.html', {'snippets': snippets})

@login_required
def my_snippets(request):
    snippets = request.user.snippets.all().order_by('-created_at')
    return render(request, 'snippets/snippet_list.html', {'snippets': snippets, 'my': True})

@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
            messages.success(request, 'Snippet created!')
            return redirect('my_snippets')
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_form.html', {'form': form, 'title': 'Create Snippet'})

@login_required
def snippet_update(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Snippet updated!')
            return redirect('my_snippets')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_form.html', {'form': form, 'title': 'Edit Snippet'})

@login_required
def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        snippet.delete()
        messages.success(request, 'Snippet deleted!')
        return redirect('my_snippets')
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet, 'delete': True})
