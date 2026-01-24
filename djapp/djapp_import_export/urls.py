## must add this file for every new django app with endpoints

from django.urls import path
from . import views

app_name = 'app_import_export'

urlpatterns = [
    path('', views.func_index, name='djep_index'),
    path('urlep_import/', views.func_import, name='djep_import'),
]
