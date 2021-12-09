from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('guess/', views.guess, name='guess'),
    path('guess/', views.guess, name='guess'),
]
