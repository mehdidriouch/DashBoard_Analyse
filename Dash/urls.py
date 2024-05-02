from django.contrib import admin
from django.urls import path, include

from Dash import views

urlpatterns = [
    path('', views.LoadFilePage, name='Load_File'),
    path('DashBoard', views.DashBoard_Page, name='DashBoard_Page'),

]
