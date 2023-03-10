"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("news/", views.news),
    path('news/<str:pageindex>/', views.news),
    path('detail/<int:detail_id>/', views.detail),
    path('login/', views.login),
    path('adminmain/', views.adminmain),
    path('adminmain/<str:pageindex>/', views.adminmain),
    path('admin_add/', views.admin_add),
    path('admin_edit/<int:newsid>/', views.admin_edit),
	path('admin_edit/<int:newsid>/<str:edittype>/', views.admin_edit),
	path('admin_delete/<int:newsid>/', views.admin_delete),
	path('admin_delete/<int:newsid>/<str:deletetype>/', views.admin_delete),
]
