from django.urls import path, register_converter

from . import converters, views

register_converter(converters.PubDateConverter, 'pub_date')


urlpatterns = [
    path(r'books/', views.books_view, name='books'),
    path(r'books/<pub_date:pub_date>/', views.books_view_by_date, name='books_by_date'),
]
