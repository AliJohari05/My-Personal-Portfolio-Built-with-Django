from django.shortcuts import render,get_object_or_404
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
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})