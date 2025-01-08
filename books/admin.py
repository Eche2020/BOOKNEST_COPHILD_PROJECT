from django.contrib import admin
from .models import Book, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = (
        'title', 
        'author', 
        'genre', 
        'price', 
        'stock_quantity', 
        'publication_date'
    )
    
    # Fields to use for searching
    search_fields = ('title', 'author', 'genre__name')
    
    # Filters to add on the right side of the admin page
    list_filter = ('genre', 'publication_date')
    
    # Fields to show when editing a book
    fields = (
        'title', 
        'author', 
        'genre', 
        'price', 
        'stock_quantity', 
        'publication_date', 
        'cover_image', 
        'description'
    )
    
    # Customize how date fields are displayed
    readonly_fields = ('publication_date',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # List of fields to display in the genre list view
    list_display = ('name', 'book_count')
    
    # Custom method to count books in each genre
    def book_count(self, obj):
        return obj.books.count()
    
    # Set a more descriptive column name
    book_count.short_description = 'Number of Books'

# Optional: Customize the admin site header
admin.site.site_header = 'Book Catalog Administration'
admin.site.site_title = 'Book Catalog Admin'
admin.site.index_title = 'Welcome to Book Catalog Management'