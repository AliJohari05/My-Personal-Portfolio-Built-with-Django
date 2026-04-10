from django.contrib import admin
from .models import AICreation
# Register your models here.
@admin.register(AICreation)
class AICreationAdmin(admin.ModelAdmin):
    # Display fields in admin list
    list_display = ('title', 'creation_type', 'status', 'created_on')

    # Filters for sidebar
    list_filter = ('status', 'creation_type', 'created_on')

    # Search functionality
    search_fields = ('title', 'summary', 'creation_type')

    # Auto-generate slug from title
    prepopulated_fields = {'slug': ('title',)}