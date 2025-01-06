from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_list(request):
    """Wyświetla listę wszystkich postów."""
    posts = Post.objects.all().order_by('-created_at')  # Sortowanie od najnowszego
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    """Dodawanie nowego posta."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Nie zapisujemy jeszcze w bazie
            post.author = request.user     # Ustawiamy autora na aktualnego użytkownika
            post.save()
            return redirect('post_list')  # Po zapisaniu przekierowanie na listę postów
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