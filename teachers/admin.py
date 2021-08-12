from django.contrib import admin
from teachers.models import Subject, Teacher, TeacherRole, Assign_Role
# Register your models here.
@admin.register(Subject)
class adminSubject(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']
@admin.register(Teacher)
class adminTeacher(admin.ModelAdmin):
    list_display = ('name','gender','subject')
    list_filter = ['gender']

    def subject(self, obj):
        return obj.Subject.name

@admin.register(TeacherRole)
class adminTeacherRole(admin.ModelAdmin):
    list_display = ('name','description')
@admin.register(Assign_Role)
class adminAssign(admin.ModelAdmin):
    list_display = ('teacher', 'StartDate')
    list_filter = ['StartDate']

    def teacher(self, obj):
        return obj.Teacher.name
