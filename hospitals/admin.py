from django.contrib import admin
# from .models import Hospital

# @admin.register(Hospital)
# class HospitalAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'latitude', 'longitude', 'amenity', 'healthcare')
#     search_fields = ('name', 'address')

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hospital
from .models import Hospital
# from mapwidgets.widgets import GooglePointFieldWidget

from hospitals import models

class HospitalAdmin(OSMGeoAdmin):
    default_lon = 5.1951  # Default longitude for Akure
    default_lat = 7.2571  # Default latitude for Akure
    default_zoom = 12

admin.site.register(Hospital, HospitalAdmin)

