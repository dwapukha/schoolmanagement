from django.contrib import admin
from django import forms
from  django.db.models import Sum, F
from Examination.models import Exam_Result, Grade, Exam,Exam_Type
from student.models import Student_Admission
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.


@admin.register(Exam_Result)
class AdminExamResults(admin.ModelAdmin):
    list_display = ('Admin_No','subject', 'Cat_One','Cat_Two','Average_Cat', 'Main_Marks', 'total', 'Grade')
    list_filter=('subject','Admin_No' )

    def Admin_No(self, obj):
        return obj.Student_Adminssion.id


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