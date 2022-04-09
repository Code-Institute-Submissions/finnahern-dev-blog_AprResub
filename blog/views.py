from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CreatePostForm, EditPostForm


def post_list(request):
    """
    Function to render the post_list homepage when called,
    including pagination to display 4 posts per page
    """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    """
    Function to render the post detail page when the user
    selects a specific blog post to view.
    """
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})


def add_post(request):
    """
    Function to render add_post page and submit forms
    to create new blog posts
    """
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = new_post.title.lower().replace(" ", "-")
            new_post.status = "published"
            new_post = form.save()
            post = new_post
            return render(request, "blog/post/detail.html", {"post": post})
    else:
        form = CreatePostForm()
    return render(request, "blog/post/add_post.html", {"form": form})


def edit_post(request, year, month, day, post):
    """
    Function to render edit_post page and submit forms
    to edit existing blog posts
    """
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return render(request, "blog/post/detail.html", {"post": post})
    else:
        data = {"title": post.title, "body": post.body}
        form = EditPostForm(initial=data)
    return render(request, "blog/post/edit_post.html", {"form": form})


def delete_post(request, year, month, day, post):
    """
    Function to delete existing posts from the
    user's dashboard
    """
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # post.delete()
    return dashboard(request)


@login_required
def dashboard(request):
    """
    Function to render the dashboard template, including a paginated
    list of posts authored by the current user.
    """
    object_list = Post.published.filter(author=request.user)
    paginator = Paginator(object_list, 8)  # 8 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  "blog/dashboard.html",
                  {"page": page,
                   "posts": posts})
