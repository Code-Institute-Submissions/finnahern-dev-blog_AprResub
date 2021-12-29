from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "blog"

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail"),
    # user login views
    # path("login/", views.user_login, name="login")
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
