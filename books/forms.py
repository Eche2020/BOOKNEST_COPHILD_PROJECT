from django import forms
from .models import Book, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "price", "stock_quantity", "genre", "cover_image"]
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }