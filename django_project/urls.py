"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appdorenatin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "principal"),
    path('nacional/', views.create_nacional),
    path('artilheiro/', views.create_artilheiro),
    path('artilheiro/edit/<artilheiro_id>', views.update_artilheiro),
    path('artilheiro/delete/<artilheiro_id>', views.delete_artilheiro),
    path('nacional/edit/<nacional_id>', views.update_nacional),
    path('nacional/delete/<nacional_id>', views.delete_nacional),
]
#path('nacional/', views.list_nacional),
#path('artilheiros/', views.list_artilheiro),