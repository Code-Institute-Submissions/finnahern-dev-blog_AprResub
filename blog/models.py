from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Post(models.Model):
    """Data model for blog posts"""
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the unique url for each Post object"""
        return reverse("blog:post_detail",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])

    def get_edit_url(self):
        """Returns the edit url for each Post object"""
        return reverse("blog:edit_post",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])

    def get_delete_url(self):
        """Returns the delete url for each Post object"""
        return reverse("blog:delete_post",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])
