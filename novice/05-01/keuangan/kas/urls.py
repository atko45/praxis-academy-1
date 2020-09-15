from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index),
    path('about/', views.about),
    path('penjualan/', views.penjualan),

    path('input/', views.input),
    path('<id>/delete/', views.delete),
    path('<id>/edit', views.edit),

]