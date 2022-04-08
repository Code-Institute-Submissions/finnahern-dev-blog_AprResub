from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # change password views
    path("password_change/",
         auth_views.PasswordChangeView.as_view(
            success_url="/password_change/done"),
         name="password_change"),
    path("password_change/done/",
         auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    # user registration views
    path("register/", views.register, name="register")
]
