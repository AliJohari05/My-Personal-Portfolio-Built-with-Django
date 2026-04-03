from django.contrib import admin
from .models import Project
from .models import ContactMessage
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project)
class ContactMessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactMessage)