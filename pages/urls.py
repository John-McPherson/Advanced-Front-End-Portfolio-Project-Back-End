from django.urls import path
from pages import views

urlpatterns = [
    path("pages/", views.PageList.as_view()),
    path("page/<int:pk>/", views.PageDetail.as_view()),
]
