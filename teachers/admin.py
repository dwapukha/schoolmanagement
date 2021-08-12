from django.contrib import admin
from teachers.models import Subject, Teacher, TeacherRole, Assign_Role
# Register your models here.
@admin.register(Subject)
class adminSubject(admin.ModelAdmin):
    pass
@admin.register(Teacher)
class adminTeacher(admin.ModelAdmin):
    pass
@admin.register(TeacherRole)
class adminTeacherRole(admin.ModelAdmin):
    pass
@admin.register(Assign_Role)
class adminAssign(admin.ModelAdmin):
    pass
