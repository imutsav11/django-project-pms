from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView
from .import views


urlpatterns = [

#localhost:8000/user/manager_register/
path("manager_register/",ManagerRegisterView.as_view(),name="manager_register"),
path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
path("login/",UserLoginView.as_view(),name="login"),
path("logout/",LogoutView.as_view(),name="logout"),

path("developer-dashboard/",views.DeveloperDashboardView.as_view(),name="developer-dashboard"),
path("manager-dashboard/",views.ManagerDashboardView.as_view(),name="manager-dashboard"),
]