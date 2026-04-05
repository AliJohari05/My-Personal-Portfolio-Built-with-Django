from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Post
# Create your views here.
def blog_page(request):
    category = get_object_or_404(Category, name='category_name')
    post_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)