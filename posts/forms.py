from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Powiązanie formularza z modelem Post
        fields = ['title', 'content', 'image']  # Pola, które będą widoczne w formularzu
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł posta'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Treść posta'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Tytuł posta',
            'content': 'Treść posta',
            'image': 'Dodaj obrazek',
        }
