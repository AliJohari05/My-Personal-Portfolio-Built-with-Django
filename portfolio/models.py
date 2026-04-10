from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    categories = models.ManyToManyField(ProjectCategory, related_name='projects')
    tech_stack = models.CharField(max_length=250, blank=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title

    def get_tech_list(self):
        if self.tech_stack:
            return [tech.strip() for tech in self.tech_stack.split(',')]
        return []

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.name}"