
'''
'''

from djapp.import_export.models import UserHair
from djapp.import_export.models import Coordinate
from djapp.import_export.models import Address
from djapp.import_export.models import Company
from djapp.import_export.models import UserData

from json import load as json_load
from json import dump as json_dump

from djadmin_config.settings import DATA_FILES_ROOT

from pathlib import Path
from os.path import join as os_path_join


def clean_data (raw_data_filename, cleaned_data_filename):
    '''
    Returns True if file exists.
    Returns False otherwise.
    '''
    raw_data_filename_with_path = os_path_join(DATA_FILES_ROOT, raw_data_filename)
    cleaned_data_filename_with_path = os_path_join(DATA_FILES_ROOT, cleaned_data_filename)

    file_path = Path(raw_data_filename_with_path)

    if not file_path.exists():
        return False
    
    necessary_key_list = (
        'firstName',
        'lastName',
        'email',
    )

    upper_lower_key_list = (
        'firstName',
        'lastName',
    )
    
    def check_necessary_key (user_dict, key):
        return key in user_dict
    
    def check_necessary_keys (user_dict):
        flag = True

        for item in necessary_key_list:
            flag = flag and check_necessary_key(user_dict, item)
            
        return flag
    
    def check_necessary_value (user_dict, key):
        try:
            return user_dict[key]
        except Exception as e:
            return False

    def check_necessary_values (user_dict):
        flag = True

        for item in necessary_key_list:
            flag = flag and check_necessary_value(user_dict, item)
            
        return flag

    def check_user_dict (user_dict) :
        flag = check_necessary_keys(user_dict)

        if flag:
            flag = check_necessary_values(user_dict)
        else:
            return False
        
        return flag

    def check_upper_lower (str) :
        if str == str.upper():
            return str.capitalize()
        if str == str.lower():
            return str.capitalize()
        return str
    
    def fix_upper_lower (user_dict):
        for item in upper_lower_key_list:
            user_dict[item] = check_upper_lower(user_dict[item])
    
    with open(raw_data_filename_with_path, 'r') as file:
        data = json_load(file)
    
    users = data['users']

    clean_users = []
    
    for user in users:
        if check_user_dict(user):
            # user has necessary fields
            # fix upper/lower
            fix_upper_lower(user)
            clean_users.append(user)

    # write clean_users to target file
    # json
    json_users_dict_list = {'users':clean_users}

    with open(cleaned_data_filename_with_path, 'w') as json_file:
        json_dump(json_users_dict_list, json_file, indent=4)
    
    return True
# end def clean_data()

def import_users (filename) :
    '''
    Returns True if file exists.
    Returns False otherwise.
    '''

    filename_with_path = os_path_join(DATA_FILES_ROOT, filename)

    file_path = Path(filename_with_path)

    if not file_path.exists():
        return False

    with open(filename_with_path, 'r') as file:
        data = json_load(file)
    
    users = data['users']
    
    for user in users:
        # print(user['firstName'])
        # print(user['lastName'])
        # print(user['address']['address'])
        # print(user['address']['coordinates']['lat'])
        # print(user['address']['coordinates']['lng'])

        user_hair = user['hair']

        user_address = user['address']

        user_company = user['company']

        user_company_address = user_company['address']

        obj_user_hair, created = UserHair.objects.get_or_create(
            hair_color  = user_hair['color'],
            hair_type   = user_hair['type'],
        )

        obj_user_address_coordinate, created = Coordinate.objects.get_or_create(
            latitude    = user_address['coordinates']['lat'],
            longitude   = user_address['coordinates']['lng'],
        )

        obj_user_address, created = Address.objects.get_or_create(
            address_line    = user_address['address'],
            city            = user_address['city'],
            state           = user_address['state'],
            state_code      = user_address['stateCode'],
            postal_code     = user_address['postalCode'],
            coordinate      = obj_user_address_coordinate,
            country         = user_address['country'],
        )

        obj_company_address_coordinate, created = Coordinate.objects.get_or_create(
            latitude    = user_company_address['coordinates']['lat'],
            longitude   = user_company_address['coordinates']['lng'],
        )

        obj_company_address, created = Address.objects.get_or_create(
            address_line    = user_company_address['address'],
            city            = user_company_address['city'],
            state           = user_company_address['state'],
            state_code      = user_company_address['stateCode'],
            postal_code     = user_company_address['postalCode'],
            coordinate      = obj_company_address_coordinate,
            country         = user_company_address['country'],
        )

        obj_company, created = Company.objects.get_or_create(
            department  = user_company['department'],
            name        = user_company['name'],
            title       = user_company['title'],
            address     = obj_company_address,
        )   

        obj_user_data, created = UserData.objects.get_or_create(
            first_name  = user['firstName'],
            last_name   = user['lastName'],
            maiden_name = user['maidenName'],
            age         = user['age'],
            gender      = user['gender'],
            email       = user['email'],
            phone       = user['phone'],
            username    = user['username'],
            password    = user['password'],
            birth_date  = user['birthDate'],
            image       = user['image'],
            blood_group = user['bloodGroup'],
            height      = user['height'],
            weight      = user['weight'],
            eye_color   = user['eyeColor'],
            hair        = obj_user_hair,
            ip          = user['ip'],
            address     = obj_user_address,
            company     = obj_company,
        )

    # end for
    
    return True
# end def import_users()

def delete_user_data ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    try:
        del_cnt, _ = UserData.objects.all().delete()
        return del_cnt
    except Exception as e:
        print(e)
        return 0
# end def delete_user_data()

def delete_company ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    try:
        del_cnt, _ = Company.objects.all().delete()
        return del_cnt
    except Exception as e:
        print(e)
        return 0
# end def delete_user_data()

def delete_address ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    try:
        del_cnt, _ = Address.objects.all().delete()
        return del_cnt
    except Exception as e:
        print(e)
        return 0
# end def delete_address()

def delete_coordinate ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    try:
        del_cnt, _ = Coordinate.objects.all().delete()
        return del_cnt
    except Exception as e:
        print(e)
        return 0
# end def delete_coordinate()

def delete_user_hair ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    try:
        del_cnt, _ = UserHair.objects.all().delete()
        return del_cnt
    except Exception as e:
        print(e)
        return 0
# end def delete_user_hair()

def delete_all_user_data ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    DEBUG_FUNCTION = False
    count = 0
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    count += delete_user_data()
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    count += delete_company()
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    count += delete_address()
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    count += delete_coordinate()
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    count += delete_user_hair()
    print(f"delete_all_user_data() {count = }") if DEBUG_FUNCTION else 0
    return count
# end def delete_all_user_data()
