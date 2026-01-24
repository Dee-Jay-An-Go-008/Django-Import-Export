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
from djapp.utils.utils_import import clear_all_user_data



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

def func_import_data (request):
    '''
    called from import.html
    '''

    import_users ('users.json')

    messages.success(request, 'Data Imported.')

    return redirect('app_import_export:djep_import')
# end def func_import()

def func_clear_data (request) :
    '''
    called from import.html
    '''
    count = clear_all_user_data()

    if count:
        messages.success(request, 'Data Cleared.')
    else:
        messages.error(request, 'Data Not Cleared.')

    return redirect('app_import_export:djep_import')
# end def func_clear_data()

def func_export (request):
    '''
    '''
    return render(request, 'tpl_import_export/export.html')
# end def func_index()

def func_export_data (request):
    '''
    '''
    return render(request, 'tpl_import_export/export.html')
# end def func_index()

