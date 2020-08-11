from django.test import TestCase, Client
from django.urls import reverse, resolve
from rest_framework import status
from api.views import overview, TaskList, TaskDetail, TaskCreate
from api.models import Task


class TestUrls(TestCase):

    def test_overview_resloves(self):
        url = reverse('overview')
        self.assertEquals(resolve(url).func, overview)

    def test_task_list_resloves(self):
        url = reverse('task-list')
        self.assertEquals(resolve(url).func.view_class, TaskList)

    def test_task_detail_resloves(self):
        url = reverse('task-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskDetail)

    def test_task_create_resloves(self):
        url = reverse('task-create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_overview = reverse('overview')
        self.url_task_list = reverse('task-list')
        self.url_task_detail = reverse('task-detail', args=[1])
        Task.objects.create(
            title='task1'
        )

    def test_overview(self):
        response = self.client.get(self.url_overview)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_task_list(self):
        response = self.client.get(self.url_task_list)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_task_detail_GET(self):
        response = self.client.get(self.url_task_detail)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_task_detail_PUT(self):
        response = self.client.put(self.url_task_detail, {
            'title': 'task1updated'
        }, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_task_detail_DELETE(self):
        response = self.client.delete(self.url_task_detail)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_create(self):
        response = self.client.post(reverse('task-create'), {
            'title': 'another item'
        }, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Task.objects.count(), 2)

    def test_task_create_with_no_data(self):
        response = self.client.post(reverse('task-create'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(Task.objects.count(), 1)
