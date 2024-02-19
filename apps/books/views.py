from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.books.models import Book, Author, BookGenre


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    # pk_url_kwarg = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "book"
    template_name = "books/book_detail.html"


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "books/author_list.html"


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "books/author_detail.html"


class GenreListView(ListView):
    model = BookGenre
    context_object_name = "genres"
    template_name = "books/genre_list.html"


class GenreDetailView(DetailView):
    model = BookGenre
    slug_field = 'name'
    slug_url_kwarg = 'name'
    context_object_name = "genre"
    template_name = "books/genre_detail.html"
