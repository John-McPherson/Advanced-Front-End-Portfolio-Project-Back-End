from django.urls import path
from project import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    ]

