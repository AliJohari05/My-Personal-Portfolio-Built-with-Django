from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def blog_page(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)