from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book_list/', views.book_list, name="book_list"),
    path('add-book/', views.add_book, name="add_book"),
    path('book/<int:book_id>/', views.book_detail, name="book_detail"),
    path('search/', views.search_books, name="search_books"),
]