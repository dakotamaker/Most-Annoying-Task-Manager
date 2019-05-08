"""MostAnnoyingTaskManeger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AnnoyingManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.Login.as_view(), name='login'),
    path(r'login', views.Login.as_view(), name='login'),
    path(r'register', views.Register.as_view(), name='new_user'),
    path(r'tasks', views.TaskList.as_view(), name='tasks_list'),
    path(r'tasks/delete/<task_id>', views.delete_task, name='delete_task'),
    path(r'lateTasks', views.LateTasks.as_view(), name='late_tasks'),
    path(r'profile', views.Profile.as_view(), name='user_profile'),
    path(r'profile/delete/<user_id>', views.delete_user, name='delete_user'),
    path(r'logout', views.Logout.as_view(), name='logout'),
]
