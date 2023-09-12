from django.urls import path
from .views import *
urlpatterns = [
    path('all/authors/', AllAuthors.as_view()),
    path('post/author/', PostAuthor.as_view()),
    path('change/author/<int:author_id>/', ChangeAuthor.as_view()),
    path('delete/author/<int:author_id>/', DeleteAuthor.as_view()),

    path('all/books/', AllBooks.as_view()),
    path('post/book/', PostBook.as_view()),
    path('change/book/<int:book_id>/', ChangeBook.as_view()),
    path('delete/book/<int:book_id>/', DeleteBook.as_view()),

    path('get/books/<int:aauthor_id>/', GetAuthorBook.as_view())
]