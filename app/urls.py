from app.views import TodoListAndCreate, TodoDatailChangeDelete
from django.urls import path

urlpatterns = [
    path('',TodoListAndCreate.as_view()),
    path('<int:pk>/',TodoDatailChangeDelete.as_view()),
]