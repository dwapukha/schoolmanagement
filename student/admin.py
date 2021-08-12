from django.contrib import admin
from student.models import Student_Registration, Class_Room, Dormetry, Student_Admission
# Register your models here.

@admin.register(Student_Registration)
class adminStudReg(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(Class_Room)
class AdminClassRoom(admin.ModelAdmin):
    list_display = ('name', 'stream')
    list_filter = ['stream']

@admin.register(Dormetry)
class AdminDorm(admin.ModelAdmin):
    list_display = ('name', 'cube', 'bed_number')
    list_filter = ['name']

@admin.register(Student_Admission)
class AdminStudAdmin(admin.ModelAdmin):
    pass