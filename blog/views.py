from django.shortcuts import render

# Create your views here.
def blog_page(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog_page.html', context)