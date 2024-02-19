from django.urls import path
from apps.books.views import BookListView, BookDetailView, AuthorListView, AuthorDetailView, GenreListView, \
    GenreDetailView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('genres/', GenreListView.as_view(), name='genre_list'),

    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('genres/<str:name>/', GenreDetailView.as_view(), name='genre_detail'),
]
