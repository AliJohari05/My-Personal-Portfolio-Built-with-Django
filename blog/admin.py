from django.contrib import admin
from .models import Post,Category,Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','image')
    search_fields = ('title','category','content')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)