from django.urls import path

from .views import overview, TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', overview, name='overview'),
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]
