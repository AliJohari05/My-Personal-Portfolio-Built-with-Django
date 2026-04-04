from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class AICreation(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    creation_type = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='ai_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
