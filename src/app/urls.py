from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_topic/", views.index, name="create_topic"),
    path("create_student/", views.index, name="create_student"),
    path("create_course/", views.index, name="create_course"),
]
