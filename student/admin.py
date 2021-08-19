from django.contrib import admin
from student.models import Student_Registration, Class_Room, Dormetry, Student_Admission,ID_Card,Stream
# Register your models here.

@admin.register(Student_Registration)
class adminStudReg(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(Class_Room)
class AdminClassRoom(admin.ModelAdmin):
    list_display = ('name', 'class_level')



@admin.register(Dormetry)
class AdminDorm(admin.ModelAdmin):
    list_display = ('name', 'cube', 'bed_number')
    list_filter = ['name']

@admin.register(Student_Admission)
class AdminStudAdmin(admin.ModelAdmin):
    pass

@admin.register(ID_Card)
class AdminID_Card(admin.ModelAdmin):
    pass
    #list_display = ('date_of_Admin',)

   # def Name(self, obj):
    #    return obj.Student_Registration.last_name
   # def First_Name(self, obj):
   #     return obj.Student_Registration.first_name
    #def passport(self, obj):
     #   return obj.Student_Registration.passport
    #def date_of_Admin(self, obj):
     #   return obj.Student_Registration.date_of_Admin
    #def Reg_num(self, obj):
     #   return obj.Student_Admission.studenid
@admin.register(Stream)
class AdminStream(admin.ModelAdmin):
    list_display = ('id','stream', 'classname')

    def classname(self, obj):
        return obj.Class_Room.Class_Names