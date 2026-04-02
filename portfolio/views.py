from django.shortcuts import render
from .models import Project
from blog.models import Post
from ai_lab.models import AICreation
# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    ai_creation = AICreation.objects.all()
    context = {'projects':projects,
               'posts':posts,
               'ai_creation':ai_creation}
    return render(request, 'home.html', context)
def portfolio_page(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'portfolio.html', context)
