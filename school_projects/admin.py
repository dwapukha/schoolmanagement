from django.contrib import admin
from school_projects.models import Upcoming, Projects, Partners
# Register your models here.
@admin.register(Upcoming)
class AdminUpprojects(admin.ModelAdmin):
    pass

@admin.register(Projects)
class AdminProjects(admin.ModelAdmin):
    pass

@admin.register(Partners)
class AdminPartners(admin.ModelAdmin):
    pass