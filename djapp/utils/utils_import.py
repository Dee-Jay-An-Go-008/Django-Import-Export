
'''
'''

from djapp.import_export.models import UserHair
from djapp.import_export.models import Coordinate
from djapp.import_export.models import Address
from djapp.import_export.models import Company
from djapp.import_export.models import UserData

import json

from djadmin_config.settings import DATA_FILES_ROOT

from pathlib import Path
from os.path import join as os_path_join


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
        data = json.load(file)
    
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
    count = 0
    print(f"delete_all_user_data() {count = }")
    count += delete_user_data()
    print(f"delete_all_user_data() {count = }")
    count += delete_company()
    print(f"delete_all_user_data() {count = }")
    count += delete_address()
    print(f"delete_all_user_data() {count = }")
    count += delete_coordinate()
    print(f"delete_all_user_data() {count = }")
    count += delete_user_hair()
    print(f"delete_all_user_data() {count = }")
    return count
# end def delete_all_user_data()
