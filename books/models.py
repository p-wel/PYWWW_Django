from django.db import models
from django.utils.timezone import now, timedelta


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        """Check if added book is added earlier than now() - days"""
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Author(Timestamped):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.birth_year} - )"


class Book(Timestamped):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.DateField()
    author = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.id} {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    category_description = models.TextField(blank=True)
    books = models.ManyToManyField("books.Book")






