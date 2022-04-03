from app.views import TodoListAndCreate2, TodoDatailChangeDelete2
from django.urls import path

urlpatterns = [
    path('',TodoListAndCreate2.as_view()),
    path('<int:pk>/',TodoDatailChangeDelete2.as_view()),
]