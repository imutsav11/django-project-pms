from django.contrib import admin
from django.urls import path, include

from .views import ProjectCreationView,ProjectListView,ProjectTeamCreateView,ProjectModuleCreateView
from .views import ProjectModuleListView,ProjectTeamListVIew,ProjectTaskCreateView,ProjectTaskListView
from .views import ProjectDeleteView,ProjectDetaileView,ProjectUpdateView
from .views import ProjectTeamDeleteView,ProjectTeamDetaileView,ProjectTeamUpdateView
urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("update/<int:pk>",ProjectUpdateView.as_view(),name="update_project"),
 path("delete/<int:pk>",ProjectDeleteView.as_view(),name="delete_project"),
 path("detail/<int:pk>",ProjectDetaileView.as_view(),name="detail_project"),
 path("team_create/",ProjectTeamCreateView.as_view(),name="team_create"),
 path("team_list/",ProjectTeamListVIew.as_view(),name="team_list"),
 path("module_create/",ProjectModuleCreateView.as_view(),name="module_create"),
 path("module_list/",ProjectModuleListView.as_view(),name="module_list"),
 path("task_create/",ProjectTaskCreateView.as_view(),name="task_create"),
 path("task_list/",ProjectTaskListView.as_view(),name="task_list"),
 path("update_team/<int:pk>",ProjectTeamUpdateView.as_view(),name="update_team"),
 path("delete_team/<int:pk>",ProjectTeamDeleteView.as_view(),name="delete_team"),
 path("detail_team/<int:pk>",ProjectTeamDetaileView.as_view(),name="detail_team"),

]
