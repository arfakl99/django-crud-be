from django.urls import path
from . import views
urlpatterns = [
    path("", views.students_list_create, name="students_list_create"),
    path("<int:pk>/", views.student_detail, name="student_detail"),
]
