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





# Django Book Catalog Management System

A comprehensive book catalog management system built with Django, featuring a responsive Bootstrap UI for managing books, genres, and inventory.

## Features

### User Features
- Browse books with grid-based layout
- Search books by title or author
- Filter books by genre
- View detailed book information
- Responsive design for mobile and desktop

### Admin Features
- Add, edit, and delete books
- Manage book inventory
- Upload book cover images
- Track stock quantities
- Organize books by genres
- Custom admin interface

## Technology Stack

- **Backend:** Django 4.2.7
- **Frontend:** Bootstrap 5
- **Database:** SQLite (default) / PostgreSQL (optional)
- **Image Handling:** Pillow
- **Styling:** CSS3
- **Icons:** Font Awesome

## Project Structure
```
bookstore_project/
│
├── bookstore/                  # Project Directory
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── books/                      # Books App Directory
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS)
│   ├── templates/             # HTML templates
│   │   ├── base.html         # Base template
│   │   ├── add_book.html     # Add book form
│   │   ├── book_list.html    # Book listing
│   │   ├── book_detail.html  # Book details
│   │   └── search_results.html
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── models.py             # Database models
│   ├── views.py              # View controllers
│   ├── urls.py               # App URL configuration
│   └── forms.py              # Form definitions
│
├── media/                     # User-uploaded media
│   └── book_covers/          # Book cover images
│
├── static/                    # Project-wide static files
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-book-catalog.git
cd django-book-catalog
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Main site: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`

## Models

### Book Model
- Title
- Author
- Publication Date
- Price
- Stock Quantity
- Genre (Foreign Key)
- Cover Image
- Description

### Genre Model
- Name
- Book Count (computed)

## Views

1. **Book List View**
   - URL: `/`
   - Displays all books in a grid layout
   - Filter by genre
   - Sort options

2. **Book Detail View**
   - URL: `/book/<id>/`
   - Shows comprehensive book information
   - Display cover image
   - Stock status

3. **Add Book View**
   - URL: `/add-book/`
   - Form for adding new books
   - Image upload capability

4. **Search View**
   - URL: `/search/`
   - Search by title or author
   - Filter results

## Admin Interface

The custom admin interface provides:
- Book management
- Genre management
- Stock tracking
- User management
- Customized list views
- Search and filter capabilities

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/django-book-catalog](https://github.com/yourusername/django-book-catalog)

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Font Awesome Icons
- Django Admin Interface
