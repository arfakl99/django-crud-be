from django.urls import path
from . import views
urlpatterns = [
    path("", views.students_list_create, name="students_list_create"),
    path("<int:pk>/", views.update_student, name="update_student"),
    path("<int:pk>/", views.delete_student, name="delete_student"),
]
