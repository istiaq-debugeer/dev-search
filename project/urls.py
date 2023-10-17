from django.urls import path
from . import views

urlpatterns=[
    path('projects/',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name="project"),
    path('create-project/', views.createProject, name="project"),
    path('update-project/<str:pk>', views.UpdateProject, name="edit"),
    path('delete/<str:pk>', views.DeleteProject, name="delete"),
    path('index/', views.home, name="index")
]