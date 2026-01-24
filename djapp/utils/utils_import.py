
from djapp.djapp_import_export.models import UserHair
from djapp.djapp_import_export.models import Coordinate
from djapp.djapp_import_export.models import Address
from djapp.djapp_import_export.models import Company
from djapp.djapp_import_export.models import UserData

import json

from djadmin_config.settings import DATA_FILES_ROOT

def import_users (filename) :

    with open(DATA_FILES_ROOT + '/' + filename, 'r') as file:
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
# end def import_users()

def clear_user_data ():
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
# end def clear_user_data()

def clear_company ():
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
# end def clear_user_data()

def clear_address ():
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
# end def clear_address()

def clear_coordinate ():
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
# end def clear_coordinate()

def clear_user_hair ():
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
# end def clear_user_hair()

def clear_all_user_data ():
    '''
    Clear table.
    Returns deleted record count.
    '''
    count = 0
    count += clear_user_data()
    count += clear_company()
    count += clear_address()
    count += clear_coordinate()
    count += clear_user_hair()
    return count
# end def clear_all_user_data()
