from django.db import models

# Create your models here.
from django.db import models

class AICreation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_type = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='ai_images/', blank=True, null=True)


    def __str__(self):
        return self.title
