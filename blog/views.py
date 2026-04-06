from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Post,Category
from .forms import CommentForm
# Create your views here.
def blog_page(request):
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
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_name):
    # Get the category by name, or return 404 if not found
    category = get_object_or_404(Category, name=category_name)

    # Filter posts that have this category
    posts = Post.objects.filter(categories=category).order_by('-created_on')

    # Pagination setup (same as your main blog view)
    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
    }
    # We will reuse your existing blog template or create a new one
    return render(request, 'blog/category_posts.html', context)
