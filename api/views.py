from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def overview(request):
    api_urls = {
        'GET for list of all tasks': '/task-list/',
        'GET for detail view of one task': '/task/<str:pk>/',
        'PUT for updating a task': '/task/<str:pk>/',
        'DELETE': '/task/<str:pk>/',
        'POST': '/task-create/',
    }

    return Response(api_urls)


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
