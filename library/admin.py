from django.contrib import admin
from library.models import Genre, Book, BookInstance, Author
# Register your models here.

@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BookInstance)
class AdminBookIns(admin.ModelAdmin):
    # list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]

    #def display_genre(self):
      #  """Create a string for the Genre. This is required to display genre in Admin."""
    #    return ', '.join(genre.name for genre in self.genre.all()[:3])
    #    display_genre.short_description = 'Genre'


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_Death')
    fields = ['first_name', 'last_name',('date_of_birth', 'date_of_Death')]
