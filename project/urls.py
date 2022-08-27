from django.urls import path
from project import views

urlpatterns = [
    path("project/", views.ProjectList.as_view()),
    path("project/<int:pk>/", views.ProjectDetail.as_view()),
]
