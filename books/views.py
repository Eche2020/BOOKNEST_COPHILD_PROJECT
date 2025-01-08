from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Book, Genre
from .forms import BookForm
# Create your views here.

def add_book(request):
    genres = Genre.objects.all()

    if request.method == "POST":
        # manual form handing
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        price = request.POST.get('price')
        stock_quantity = request.POST.get('stock_quantity')
        genre_id = request.POST.get('genre_id')
        cover_image = request.FILES.get('cover_image')
        description = request.POST.get('description')

        try:
            # get the genre instance
            genre = Genre.objects.get(id=genre_id)

            # Create the Book
            book = Book.objects.create(
                title=title,
                author=author,
                publication_date=publication_date,
                price=price,
                stock_quantity=stock_quantity,
                genre=genre,
                cover_image=cover_image,
                description=description                
            )

            messages.success(request, f'Book "{title}" added successfully!')
            return redirect('book_list')

        except Exception as e:
            messages.error(request, f'Error adding book: {str(e)}')            
    return render(request, 'add_book.html', {'genres': genres})

def book_list(request):
    books = Book.objects.all().order_by('-id')
    genres = Genre.objects.all()
    return render(request, "book_list.html", {'genres': genres, 'books':books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})

def search_books(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return render(request, "search_result.html", {"query": query,"books":books})

def home(request):
    return render(request, "index.html")