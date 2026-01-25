from django.shortcuts import render
from django.shortcuts import redirect

from .models import UserHair
from .models import Coordinate
from .models import Address
from .models import Company
from .models import UserData

import json

from djadmin_config.settings import DATA_FILES_ROOT

### import to use django messages framework
from django.contrib import messages

from djapp.utils.utils_import import import_users
from djapp.utils.utils_import import delete_all_user_data
from djapp.utils.utils_import import clean_data

from djadmin_config.settings import EXPORT_FILES_URL

from djapp.utils.utils_export import export_files

# Create your views here.

## using template:

def func_index (request):
    '''
    '''
    return render(request, 'tpl_import_export/index.html')
# end def func_index()

def func_import (request):
    '''
    '''
    return render(request, 'tpl_import_export/import.html')
# end def func_index()

def func_clean_data (request):
    '''
    called from import.html
    '''
    clean_data_flag = clean_data('users_raw.json', 'users_formatted.json')
    if clean_data_flag:
        messages.success(request, 'Data Cleaned.')
    else:
        messages.error(request, 'Data Not Cleaned.')
    return redirect('app_import_export:djep_import')
# end def func_clean_data()

def func_import_data (request):
    '''
    called from import.html
    '''

    import_users_flag = import_users('users_formatted.json')

    if import_users_flag:
        messages.success(request, 'Data Imported.')
    else:
        messages.error(request, 'Data Not Imported.')

    return redirect('app_import_export:djep_import')
# end def func_import()

def func_delete_data (request) :
    '''
    called from import.html
    '''
    count = delete_all_user_data()

    if count:
        messages.success(request, 'Data Deleted.')
    else:
        messages.error(request, 'Data Not Deleted.')

    return redirect('app_import_export:djep_import')
# end def func_delete_data()

def func_export (request):
    '''
    '''
    return render(request, 'tpl_import_export/export.html')
# end def func_index()

def func_export_data (request):
    '''
    '''

    json_filename, csv_filename, export_record_count = export_files()

    json_filename_url = EXPORT_FILES_URL + json_filename
    csv_filename_url  = EXPORT_FILES_URL + csv_filename

    if export_record_count == 0:
        messages.error(request, 'No Data Exported.')

    context = {
        'export_record_count'   : export_record_count,
        'json_filename_url'     : json_filename_url,
        'csv_filename_url'      : csv_filename_url,
    }

    return render(request, 'tpl_import_export/export.html', context)
# end def func_index()

