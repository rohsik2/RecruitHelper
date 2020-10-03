# from django.conf.urls import url
from . import views
# from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
]
