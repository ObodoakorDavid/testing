from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='home' ),
    path('create/', views.todo_create, name='create'),
    path('created/', views.todo_created ),
    path('<int:id>/delete/', views.todo_delete, name='delete'),
    path('<int:id>/update', views.todo_update, name='update'),
    path('todo_updated/', views.todo_updated)
]