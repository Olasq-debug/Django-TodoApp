from django.urls import path
from .views import TodoListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name = 'home' ),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name = 'details'),
    path('create/', TaskCreateView.as_view(), name = 'task-create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name = 'task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name = 'task-delete')
]