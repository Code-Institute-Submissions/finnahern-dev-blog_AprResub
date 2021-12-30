from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, CreatePostForm


def post_list(request):
    """
    Function to render the post_list homepage when called,
    including pagination to display 4 posts per page
    """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # 4 posts in each page
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


def user_login(request):
    """
    Function to render and authenticate the user login form
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated "\
                                        "successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {"form": form})


@login_required
def dashboard(request):
    """
    Function to render the dashboard template, including a paginated
    list of posts authored by the current user 
    """
    object_list = Post.published.filter(author=request.user)
    paginator = Paginator(object_list, 4) # 4 posts in each page
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


def register(request):
    """
    Function to register new user accounts.
    """
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but don't save it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data["password"])
            # Save the user object
            new_user.save()
            return render(request,
                        "blog/register_done.html",
                        {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                "blog/register.html",
                {"user_form": user_form})
