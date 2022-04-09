from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/",
         views.post_detail,
         name="post_detail"),
    # user dashboard views
    path("dashboard/", views.dashboard, name="dashboard"),
    # CRUD views for blog posts
    path("add_post/", views.add_post, name="add_post"),
    path("edit_post/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/",
         views.edit_post,
         name="edit_post"),
    path("delete_post/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/",
         views.delete_post,
         name="delete_post"),
]
