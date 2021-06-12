from django.urls import path

from sapp import views

urlpatterns = [
    path('', views.index, name='index'),

]