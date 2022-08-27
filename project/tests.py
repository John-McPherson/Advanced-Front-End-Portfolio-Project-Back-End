from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project

class ProjectListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='john', password='pass')

    def test_can_list_projects(self):
        john = User.objects.get(username='john')
        Project.objects.create(owner=john, title='a title')
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_project(self):
        self.client.login(username='john', password='pass')
        response = self.client.post('/project/', {'title': 'a title'})
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_project(self):
        response = self.client.post('/project/', {'title': 'a title'})
        count = Project.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




