from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q,Count
from taggit.models import Tag

from .models import Post, Category, Comment
from .forms import CommentForm
# Create your views here.
def blog_page(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-created_on')
    tags = Tag.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(posts, 4)
    try:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    categories = Category.objects.annotate(post_count=Count('post'))
    recent_posts = Post.objects.all().order_by('-created_on')[:3]

    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'recent_posts': recent_posts,
        'tags': tags
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True, parent__isnull=True)
    tags = Tag.objects.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                new_comment.parent = parent_comment

            new_comment.save()
            # Redirect to the same page to prevent duplicate form submissions
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'tags': tags
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


def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    query = request.GET.get('q')
    tags = Tag.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(posts, 4)
    try:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    categories = Category.objects.annotate(post_count=Count('post'))
    recent_posts = Post.objects.all().order_by('-created_on')[:3]

    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'recent_posts': recent_posts,
        'tags': tags
    }

    return render(request, 'blog/blog.html', context)