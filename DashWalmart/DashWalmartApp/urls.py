from django.urls import path

from DashWalmartApp import views


urlpatterns = [
    path('', views.new, name='new'),
    path('index/',views.index,name='index'),
    path('prediction/',views.prediction,name='prediction'),
]