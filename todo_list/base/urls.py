from django.urls import path
from .views import TaskList, TaskDetail, TaskCreat

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create', TaskCreat.as_view(), name='task-create'),
]
