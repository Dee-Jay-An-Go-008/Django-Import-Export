
'''
'''

from djapp.import_export.models import UserHair
from djapp.import_export.models import Coordinate
from djapp.import_export.models import Address
from djapp.import_export.models import Company
from djapp.import_export.models import UserData

from json import dump as json_dump
from csv import DictWriter as csv_DictWriter
from csv import QUOTE_ALL
from os.path import join as os_path_join

from djadmin_config.settings import DATA_FILES_ROOT
from djadmin_config.settings import EXPORT_FILES_ROOT
from djadmin_config.settings import DATE_TIME_STRING_FORMAT_FOR_FILENAME

from .utils_dict import flatten_dict

from datetime import datetime

from django.forms.models import model_to_dict

def export_files () :
    '''
    Returns (json, csv) filenames.
    '''
    now = datetime.now()

    filename_datetime_part = now.strftime(DATE_TIME_STRING_FORMAT_FOR_FILENAME)

    json_filename = 'userdata_' + filename_datetime_part + '.json'
    csv_filename = 'userdata_' + filename_datetime_part + '.csv'

    json_filename_with_path = os_path_join(EXPORT_FILES_ROOT, json_filename)
    csv_filename_with_path = os_path_join(EXPORT_FILES_ROOT, csv_filename)

    def get_user_hair_dict (pk_id) :
        obj_instance = UserHair.objects.filter(pk=pk_id)[0]
        obj_dict = model_to_dict(obj_instance, fields=UserHair.fields_list())
        return obj_dict
    # end def get_user_hair_dict()

    def get_coordinate_dict (pk_id) :
        obj_instance = Coordinate.objects.filter(pk=pk_id)[0]
        obj_dict = model_to_dict(obj_instance, fields=Coordinate.fields_list())
        return obj_dict
    # end def get_coordinate_dict()

    def get_address_dict (pk_id) :
        obj_instance = Address.objects.filter(pk=pk_id)[0]
        obj_dict = model_to_dict(obj_instance, fields=Address.fields_list())
        # replace Coordinate
        obj_dict['coordinate'] = get_coordinate_dict(obj_dict['coordinate'])
        return obj_dict
    # end def get_address_dict()

    def get_company_dict (pk_id) :
        obj_instance = Company.objects.filter(pk=pk_id)[0]
        obj_dict = model_to_dict(obj_instance, fields=Company.fields_list())
        # replace Address
        obj_dict['address'] = get_address_dict(obj_dict['address'])
        return obj_dict
    # end def get_company_dict()

    def get_user_data_dict (obj_instance):
        obj_dict = model_to_dict(obj_instance, fields=UserData.fields_list())
        # replace UserHair
        obj_dict['hair'] = get_user_hair_dict(obj_dict['hair'])
        # replace Address
        obj_dict['address'] = get_address_dict(obj_dict['address'])
        # replace Company
        obj_dict['company'] = get_company_dict(obj_dict['company'])
        return obj_dict
    # end def get_user_data_dict()

    def get_all_users_dict_list () :
        users_dict_list = []
        users = UserData.objects.all()

        for user in users:
            user_dict = get_user_data_dict(user)
            users_dict_list.append(user_dict)

        return users_dict_list
    # end def get_all_users_dict_list()

    users_dict_list = get_all_users_dict_list()

    record_count = len(users_dict_list)

    # json
    json_users_dict_list = {'users':users_dict_list}

    with open(json_filename_with_path, 'w') as json_file:
        json_dump(json_users_dict_list, json_file, indent=4)
    
    # csv
    if record_count != 0:
        user_dict_sample = users_dict_list[0]
        csv_field_names = flatten_dict(user_dict_sample).keys()

        with open(csv_filename_with_path, 'w', newline='') as file:
            writer = csv_DictWriter(file, fieldnames=csv_field_names, quoting=QUOTE_ALL)
            writer.writeheader()
            for item in users_dict_list:
                writer.writerow(flatten_dict(item))

    return (json_filename, csv_filename, record_count)
# end def export_files ()
