from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


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
                    return HttpResponse("Authenticated "
                                        "successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "user/login.html", context)


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
                          "user/register_done.html",
                          {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()

    context = {"user_form": user_form}

    return render(request, "user/register.html", context)
