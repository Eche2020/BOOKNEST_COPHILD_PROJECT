# FINAL PROJECT WITH COPHILD 

TITLE: Online Book Store

DESCRIPTION: Build a simple application for managing a catalog of books, where users can browse books and administrative staff can manage the inventory.

Features:

Models:
 - Book: Contains details about a book Fields include:
    -`title`(string)
    -`author` (string)
    -`publication_date` (date)
    -`price` (decimal)
    -`stock_quantity` (integer)
    -`genre`(foreign key to Genre)


- Genre: Represents book categoriesFields include:
   - `name`(string)

FOR DJANGO TEMPLATES
Views:

1. Add a New Book
- URL: `add-book/`
- Functionality: An admin form where new books can be added to the inventory.

# SOME IMPORT INCLUDE
from.django.shortcuts import render, redirect
from .models import Book, Genre

def add_book(request):

if request.method == "POST":
# write your code to process the sent in data

return render(request, "add_book.html, {# pass things you have to send to the frontend template})

2. List All Books
- URL: `/book/<int: book_id>
-Functionality: Display detailed information about a specific book.

def book_detail(request, book_id):
# code to get book by its id

book = # your query code
return render(request, "book_detail.html", {"book":book})

3.  