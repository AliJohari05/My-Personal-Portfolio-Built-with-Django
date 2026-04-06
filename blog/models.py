from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # To fix the plural spelling in Django Admin (Categories instead of Categorys)
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name="Your Name")
    body = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at'] 

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
