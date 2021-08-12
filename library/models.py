from django.db import models
import uuid #Required for unique book instances
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre(e.g Science Fiction)')
    def __del__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField(Genre, help_text='Select genre for this book')

    def __del__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reversed('book-detail', args= [str(self.id)])
class BookInstance(models.Model):
    """The model represents a specific copy of the book that can be borrowed from the library."""
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back= models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Researved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability',
                              )
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.id} ({self.book.title})'
class Author(models.Model):
    """Model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_Death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reversed('author-detail', args = [str(self.id)])
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'




