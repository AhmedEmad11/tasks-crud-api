from django.urls import path

from .views import overview, TaskList, taskDetail, taskCreate, taskUpdate, taskDelete
urlpatterns = [
    path('', overview, name='overview'),
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-detail/<str:pk>/', taskDetail, name='task-detail'),
    path('task-update/<str:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', taskDelete, name='task-delete'),
]