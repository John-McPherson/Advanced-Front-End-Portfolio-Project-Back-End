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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProjectDetailViewTests(APITestCase):
    def setUp(self):
        john = User.objects.create_user(username='john', password='pass')
        adam = User.objects.create_user(username='adam', password='pass')
        Project.objects.create(owner=john, title='a title')
        Project.objects.create(owner=adam, title='some other title')

    def test_logged_in_user_can_retrieve_project_using_valid_id(self):
        self.client.login(username='john', password='pass')
        response = self.client.get('/project/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_retrieve_project_using_valid_id(self):
        response = self.client.get('/project/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_retrieve_project_using_invalid_id(self):
        response = self.client.get('/project/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_project(self):
        self.client.login(username='john', password='pass')
        response = self.client.put('/project/1/', {'title': 'a new title'})
        project = Project.objects.filter(pk=1).first()
        self.assertEqual(project.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_projects_they_dont_own(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/project/1/', {'title': 'a new title'})
        project = Project.objects.filter(pk=1).first()
        self.assertEqual(project.title, 'a title')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)









