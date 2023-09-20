from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    # telling django to delete if the user is null del post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        # this is for create post
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
class Images(models.Model):
    """docstring for uploading images."""
    image = models.ImageField(default="default", upload_to="images")
    description = models.CharField(max_length=100)
