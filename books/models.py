from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, help_text="Upload a book cover image")    
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.title} by {self.author}"