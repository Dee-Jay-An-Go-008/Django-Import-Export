from django.db import models

# Create your models here.

class UserHair (models.Model) :
    hair_color  = models.CharField (max_length=20, blank=True, null=True)
    hair_type   = models.CharField (max_length=20, blank=True, null=True)
    ## for export
    custom_field_names = {
        'hair_color' : 'color',
        'hair_type' : 'type',
    }
    def fields_list ():
        '''
        Returns a list of field names.
        '''
        return [
            'hair_color',
            'hair_type',
        ]
    def __str__ (self) : 
        return self.hair_color + '  ' + self.hair_type

class Coordinate (models.Model) :
    latitude    = models.FloatField(blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    ## for export
    custom_field_names = {
        'latitude' : 'lat',
        'longitude' : 'lng',
    }
    def fields_list ():
        '''
        Returns a list of field names.
        '''
        return [
            'latitude',
            'longitude',
        ]
    def __str__ (self) : 
        return str(self.latitude) + '  ' + str(self.longitude)

class Address (models.Model) :
    address_line    = models.CharField (max_length=200, blank=True, null=True)
    city            = models.CharField (max_length=200, blank=True, null=True)
    state           = models.CharField (max_length=200, blank=True, null=True)
    state_code      = models.CharField (max_length=5, blank=True, null=True)
    postal_code     = models.CharField (max_length=25, blank=True, null=True)
    coordinate      = models.ForeignKey(Coordinate, on_delete=models.DO_NOTHING, blank=True, null=True)
    country         = models.CharField (max_length=200, blank=True, null=True)
    ## for export
    custom_field_names = {
        'address_line' : 'address',
        'city' : 'city',
        'state' : 'state',
        'state_code' : 'stateCode',
        'postal_code' : 'postalCode',
        'coordinate' : 'coordinates',
        'country' : 'country',
    }
    def fields_list ():
        '''
        Returns a list of field names.
        '''
        return [
            'address_line',
            'city',
            'state',
            'state_code',
            'postal_code',
            'coordinate',
            'country',
        ]
    def __str__ (self) : 
        return self.address_line + '  ' + self.city

class Company (models.Model) :
    department  = models.CharField (max_length=200, blank=True, null=True)
    name        = models.CharField (max_length=200, blank=True, null=True)
    title       = models.CharField (max_length=200, blank=True, null=True)
    address     = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)
    ## for export
    custom_field_names = {
        'department' : 'department',
        'name' : 'name',
        'title' : 'title',
        'address' : 'address',
    }
    def fields_list ():
        '''
        Returns a list of field names.
        '''
        return [
            'department',
            'name',
            'title',
            'address',
        ]
    def __str__ (self) : 
        return self.name + '  ' + self.department

class UserData (models.Model):
    first_name  = models.CharField (max_length=200, blank=True, null=True)
    last_name   = models.CharField (max_length=200, blank=True, null=True)
    maiden_name = models.CharField (max_length=200, blank=True, null=True)
    age         = models.IntegerField(blank=True, null=True)
    gender      = models.CharField (max_length=20, blank=True, null=True)
    email       = models.CharField (max_length=200, blank=True, null=True)
    phone       = models.CharField (max_length=50, blank=True, null=True)
    username    = models.CharField (max_length=50, blank=True, null=True)
    password    = models.CharField (max_length=50, blank=True, null=True)
    birth_date  = models.CharField (max_length=50, blank=True, null=True)
    image       = models.CharField (max_length=300, blank=True, null=True)
    blood_group = models.CharField (max_length=4, blank=True, null=True)
    height      = models.FloatField(blank=True, null=True)
    weight      = models.FloatField(blank=True, null=True)
    eye_color   = models.CharField (max_length=20, blank=True, null=True)
    hair        = models.ForeignKey(UserHair, on_delete=models.DO_NOTHING, blank=True, null=True)
    ip          = models.CharField (max_length=42, blank=True, null=True)
    address     = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)
    company     = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=True, null=True)
    ## for export
    custom_field_names = {
        'first_name' : 'firstName',
        'last_name' : 'lastName',
        'maiden_name' : 'maidenName',
        'age' : 'age',
        'gender' : 'gender',
        'email' : 'email',
        'phone' : 'phone',
        'username' : 'username',
        'password' : 'password',
        'birth_date' : 'birthDate',
        'image' : 'image',
        'blood_group' : 'bloodGroup',
        'height' : 'height',
        'weight' : 'weight',
        'eye_color' : 'eyeColor',
        'hair' : 'hair',
        'ip' : 'ip',
        'address' : 'address',
        'company' : 'company',
    }
    # def foreign_key_list ():
    #     '''
    #     Returns a list of foreign key names.
    #     '''
    #     return [
    #         'hair',
    #         'address',
    #         'company',
    #     ]
    def fields_list ():
        '''
        Returns a list of field names.
        '''
        return [
            'first_name',
            'last_name',
            'maiden_name',
            'age',
            'gender',
            'email',
            'phone',
            'username',
            'password',
            'birth_date',
            'image',
            'blood_group',
            'height',
            'weight',
            'eye_color',
            'hair',
            'ip',
            'address',
            'company',
        ]
    def __str__ (self) : 
        return self.first_name + '  ' + self.last_name
