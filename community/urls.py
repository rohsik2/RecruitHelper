# from django.conf.urls import url
from . import views
# from django.contrib import admin
from django.urls import path 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cutline/', views.cutline, name='cutline'),
    path('date/', views.left_day, name='left_day'),
    path('prepare/',views.prepare, name='prepare'),
]
