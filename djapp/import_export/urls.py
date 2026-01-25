## must add this file for every new django app with endpoints

from django.urls import path
from . import views

app_name = 'app_import_export'

urlpatterns = [
    path('', views.func_index, name='djep_index'),
    path('import/', views.func_import, name='djep_import'),
    path('clean_data/', views.func_clean_data, name='djep_clean_data'),
    path('import_data/', views.func_import_data, name='djep_import_data'),
    path('delete_data/', views.func_delete_data, name='djep_delete_data'),
    path('export/', views.func_export, name='djep_export'),
    path('export_data/', views.func_export_data, name='djep_export_data'),
]
