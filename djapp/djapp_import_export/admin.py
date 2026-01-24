from django.contrib import admin

# Register your models here.

from .models import UserHair
from .models import Coordinate
from .models import Address
from .models import Company
from .models import UserData

admin.site.register(UserHair)
admin.site.register(Coordinate)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(UserData)
