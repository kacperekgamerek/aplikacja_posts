from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.post_list, name='post_list'), # Strona główna - lista postów
    path('post/new/', views.post_create, name='post_create'), # Formularz tworzenia posta
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # Edycja posta
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),  # Usuwanie posta
]
