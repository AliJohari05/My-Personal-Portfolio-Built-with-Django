from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','image','category')
    search_fields = ('title','category','content')
admin.site.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
admin.site.register(Category)