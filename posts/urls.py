from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),                # Strona główna - lista postów
    path('post/new/', views.post_create, name='post_create'),   # Formularz tworzenia posta
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # Edycja posta
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),  # Usuwanie posta
]
