from django.contrib import admin
from school_Activities.models import School_term, School_Activity, Half_term,Holidays
# Register your models here.
@admin.register(School_Activity)
class AdminSchAct(admin.ModelAdmin):
    pass

@admin.register(School_term)
class AdminSchTerm(admin.ModelAdmin):
    pass

@admin.register(Half_term)
class AdminHalfterm(admin.ModelAdmin):
    pass

@admin.register(Holidays)
class AdminHolidays(admin.ModelAdmin):
    pass