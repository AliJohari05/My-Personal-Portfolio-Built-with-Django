from django.shortcuts import render,get_object_or_404,redirect
from .models import Project,ContactMessage
from django.contrib import messages
from blog.models import Post
from ai_lab.models import AICreation
from .forms import ContactForm
from django.core.paginator import Paginator
# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    ai_creation = AICreation.objects.all()
    context = {'projects':projects,
               'posts':posts,
               'ai_creation':ai_creation}
    return render(request, 'portfolio\home.html', context)
def portfolio_page(request):
    project_list = Project.objects.all().order_by('-created_on')
    paginator = Paginator(project_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'portfolio\portfolio.html', context)
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio\project_detail.html', {'project': project})
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # message saves in db
            messages.success(request, 'Your message has been sent successfully! Thank you.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})