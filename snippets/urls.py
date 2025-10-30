
from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet_list, name='snippet_list'),
    path('my/', views.my_snippets, name='my_snippets'),
    path('create/', views.snippet_create, name='snippet_create'),
    path('register/', views.register, name='register'),
    path('<int:pk>/edit/', views.snippet_update, name='snippet_update'),
    path('<int:pk>/delete/', views.snippet_delete, name='snippet_delete'),
]