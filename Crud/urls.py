"""Crud URL Configuration

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
from Crud import views 
from enroll import views as cr
from Markssheet import views as mr



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('add_show/',cr.add_show,name="add_show"),
    path('delete/<int:id>/',cr.delete_data,name="deletedata"),
    path('<int:id>/',cr.update_data,name="updatedata"),
    path('Markssheet<str:name>/',mr.Markssheet1,name='Markssheet'),
    path('deletemarks/<str:name>/',mr.delete_marks,name='deletemarks'),
    path('updatemarks<int:id>/',mr.update_marks,name="updatemarks"),
    path('set/',views.setcookie),
    path('get/',views.getcookie),
    path('del/',views.delcookie)

]
