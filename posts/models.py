from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)  # Tytuł posta
    content = models.TextField()              # Treść posta
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor (powiązanie z użytkownikiem)
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia
    updated_at = models.DateTimeField(auto_now=True)      # Data ostatniej edycji

    def __str__(self):
        return self.title
