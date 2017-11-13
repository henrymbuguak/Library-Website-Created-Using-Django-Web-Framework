from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=250, help_text='Enter the book genre(e.g. Romance, History e.t.c)')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death= models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['date_of_birth']


class Language(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the language used to write the book')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1500, help_text='Give a brief description of the book')
    isbn = models.CharField('ISBN', max_length= 13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
                            )
    genre = models.ManyToManyField(Genre, help_text='Select genre of the book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique id for a specific book in the library'
                          )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=250)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintainance'),
        ('o', 'On loan'),
        ('a', 'available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m', blank=True, help_text='Book Availability')

    class Meta:
        ordering = ['-due_back']

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)

