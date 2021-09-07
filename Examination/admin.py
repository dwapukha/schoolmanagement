from django.contrib import admin
from django import forms
from  django.db.models import Sum, F
from Examination.models import Exam_Result, Grade, Exam,Exam_Type
# Register your models here.


@admin.register(Exam_Result)
class AdminExamResults(admin.ModelAdmin):

    list_display = ('subject', 'Cat_One','Cat_Two', 'Main_Marks', 'total', 'Grade')






@admin.register(Grade)
class AdminGrade(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Exam)
class AdminExam(admin.ModelAdmin):
    list_display = ( 'id','start_Date','Exam_type')

    def Exam_type(self, obj):
        return obj.Exam_Type.Exam_type

@admin.register(Exam_Type)
class AdminExam_Type(admin.ModelAdmin):
    list_display = ('name', 'Exam_type','description')