from django.contrib import admin
from .models import AICreation
# Register your models here.
@admin.register(AICreation)
class AICreationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('title','creation_type','image','created_on')
