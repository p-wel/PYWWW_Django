from django.db import models
from django.utils.timezone import now, timedelta


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        """Check if created post is older than now() - days"""
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    content = models.TextField(verbose_name="Treść")
    published = models.BooleanField(verbose_name="Opublikowany", default=False)
    sponsored = models.BooleanField(verbose_name="Sponsorowany", default=False)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    example_file = models.FileField(upload_to='posts/esamples', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d", null=True, blank=True, width_field="image_width")
    tags = models.ManyToManyField('tags.Tag', related_name="posts")

    def __str__(self):
        return f"{self.id} {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField('posts.Post', related_name="categories")
