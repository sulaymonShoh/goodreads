from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from apps.shared.models import AbstractModel


class LanguageChoice(models.TextChoices):
    UZBEK = "UZ", "O'zbekcha"
    ARABIC = "AR", "Arabic"
    ENGLISH = "EN", "English"
    FRENCH = "FR", "French"
    RUSSIAN = "RU", "Russian"


class Book(AbstractModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    published = models.DateField()
    isbn = models.CharField(unique=True, max_length=128)
    language = models.CharField(max_length=14, choices=LanguageChoice.choices)
    page = models.IntegerField()
    cover = models.ImageField(upload_to="books/cover/%Y/%m/%d")
    genre = models.ManyToManyField("books.BookGenre", related_name="books")
    authors = models.ManyToManyField("books.Author", related_name="books")


class Author(AbstractModel):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=56)
    website = models.URLField()
    avatar = models.ImageField(upload_to="authors/avatar/%Y/%m/%d")
    about = models.TextField()


class BookGenre(AbstractModel):
    name = models.CharField(max_length=28)


class BookReview(AbstractModel):
    body = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    like_count = models.IntegerField(default=0)
