from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login

def post_list(request):
    """Wyświetla listę wszystkich postów."""
    posts = Post.objects.all().order_by('-created_at')  # Sortowanie od najnowszego
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')  # Przekierowanie na stronę z listą postów
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_edit(request, post_id):
    """Edycja istniejącego posta."""
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Sprawdzamy, czy post istnieje i należy do użytkownika
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Przekierowanie na listę postów
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})

@login_required  # Zapewnia, że użytkownik jest zalogowany przed usunięciem posta
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Pobieramy post na podstawie ID

    # Sprawdzamy, czy użytkownik jest autorem posta
    if post.author != request.user:
        return redirect('post_list')  # Jeśli nie jesteś autorem, przekieruj na listę postów

    if request.method == 'POST':
        post.delete()  # Usuwamy post z bazy danych
        return redirect('post_list')  # Po usunięciu przekierowujemy na listę postów

    # Jeśli to GET, wyświetlamy stronę potwierdzenia usunięcia
    return render(request, 'posts/post_confirm_delete.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('post_list'))  # Możesz przekierować na stronę główną
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})