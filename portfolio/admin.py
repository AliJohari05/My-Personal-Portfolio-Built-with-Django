from django.contrib import admin
from .models import Project,ProjectCategory
from .models import ContactMessage
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title','created_on','image','tech_stack')
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name','email','created_at')
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('name','slug','created_on')