from django.contrib import admin
from teachers.models import Teacher
from timetabling.models import Ref_Calender , Class_Stream, Ref_Period, Ref_Subject, Ref_Day,Planned_Timetable,Generated_Timetable,Master_Timetable
# Register your models here.
@admin.register(Ref_Calender)
class AdminCal(admin.ModelAdmin):
    list_display = ('Day','Date_and_Time')
    list_filter = ['Day']

@admin.register(Ref_Day)
class AdminDay(admin.ModelAdmin):
    list_display = ('Day_Name', 'Day_Number')

@admin.register(Ref_Period)
class AdminPeriod(admin.ModelAdmin):
    list_display = ('id','Period_Start_Time', 'Period_Start_End')

@admin.register(Ref_Subject)
class AdminSub(admin.ModelAdmin):
    pass
@admin.register(Planned_Timetable)
class AdminPlanned(admin.ModelAdmin):
     list_display = ('Day_Name','Period_Number','Subject')

     def Day_Name(self, obj):
         return obj.Ref_Day.Day_Name

     def Period_Number(self, obj):
         return obj.Ref_Period.id
     def Subject(self, obj):
         return obj.Ref_Subject.Subject
Planned_Timetable.objects.all()

@admin.register(Generated_Timetable)
class AdminGenTimet(admin.ModelAdmin):
    list_display = ('Day_Name', 'Teacher','Class_Name', 'Stream_Name')

    def Day_Name(self, obj):
        return obj.Ref_Day.Day_Name

    def Time(self, obj):
        return obj.Ref_Period.id

    def Subject(self, obj):
        return obj.Ref_Subject.Subject

    def Teacher(self, obj):
        return obj.Teacher.name
    def Class_Name(self, obj):
        return obj.Class_Stream.Class_Name
    def Stream_Name(self, obj):
        return obj.Class_Stream.Stream_Name
    #Teacher.short_description = "Teacher"
    list_filter = ['Teacher']
@admin.register(Class_Stream)
class AdminClassStream(admin.ModelAdmin):

    list_display = ('Class_Name', 'Stream_Name')
    list_filter = ['Class_Name', 'Stream_Name']
Class_Stream.objects.all()