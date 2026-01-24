from django.db import models

# Create your models here.

class UserHair (models.Model) :
    hair_color  = models.CharField (max_length=20, blank=True, null=True)
    hair_type   = models.CharField (max_length=20, blank=True, null=True)

class Coordinate (models.Model) :
    latitude    = models.FloatField(blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)

class Address (models.Model) :
    address_line    = models.CharField (max_length=200, blank=True, null=True)
    city            = models.CharField (max_length=200, blank=True, null=True)
    state           = models.CharField (max_length=200, blank=True, null=True)
    state_code      = models.CharField (max_length=5, blank=True, null=True)
    postal_code     = models.CharField (max_length=25, blank=True, null=True)
    coordinate      = models.ForeignKey(Coordinate, on_delete=models.DO_NOTHING, blank=True, null=True)
    country         = models.CharField (max_length=200, blank=True, null=True)

class Company (models.Model) :
    department  = models.CharField (max_length=200, blank=True, null=True)
    name        = models.CharField (max_length=200, blank=True, null=True)
    title       = models.CharField (max_length=200, blank=True, null=True)
    address     = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)

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




