from django.contrib import *
from django.urls import path, include 
from . import views


'''
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
'''

urlpatterns = [
    path('', views.info, name='info'),
    path('', include('django.contrib.auth.urls')),
    path('sign_in', views.sign_in, name='sign_in'),
]