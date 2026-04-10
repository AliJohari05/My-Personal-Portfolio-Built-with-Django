from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class AICreation(models.Model):
    # Status choices for the AI experiment
    STATUS_CHOICES = (
        ('concept', 'Concept / Idea'),
        ('training', 'Training Model'),
        ('testing', 'Testing & Evaluation'),
        ('completed', 'Completed'),
        ('deployed', 'Deployed / Live'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True, help_text="URL friendly title")
    # Added summary for list views
    summary = models.CharField(max_length=255, blank=True, help_text="Short description for the list view")
    description = HTMLField()
    creation_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    link = models.URLField(blank=True)
    colab_link = models.URLField(blank=True, null=True, help_text="Link to Google Colab Notebook")
    github_link = models.URLField(blank=True, null=True, help_text="Link to GitHub Repository")
    image = models.ImageField(upload_to='ai_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Added to track modifications

    class Meta:
        # Order by newest first
        ordering = ['-created_on']

    def __str__(self):
        return self.title
