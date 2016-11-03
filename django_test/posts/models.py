from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
    )
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="like_post_set",
        through="likes.Like",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "http://placehold.it/350x150"

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
