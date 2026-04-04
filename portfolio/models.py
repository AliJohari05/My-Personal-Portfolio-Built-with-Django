from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    technology = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.name}"