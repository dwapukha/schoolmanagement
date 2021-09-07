from django.contrib import admin
from transport.models import Conductor,Bus, Driver,Route

# Register your models here.
@admin.register(Conductor)
class AdminConductor(admin.ModelAdmin):
    list_display = ('name', 'Gender', 'LicenceNo', 'Contact')
@admin.register(Bus)
class AdminBus(admin.ModelAdmin):
    list_display = ('Bus_Plate_Number','Bus_name', 'capacity')
@admin.register(Driver)
class AdminDriver(admin.ModelAdmin):
    list_display = ('name','Gender','LicenceNo','Contact')
@admin.register(Route)
class AdminRoute(admin.ModelAdmin):
    list_display = ('Route_Name','pick_point','dropoff','time')