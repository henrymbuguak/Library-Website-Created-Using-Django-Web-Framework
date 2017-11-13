from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()
    num_genre = Genre.objects.count()
    book_title = Book.objects.filter(title__contains='hands').count()
    return render(
        request,
        'catalog/index.html',
        {'num_books': num_books, 'num_instances': num_instance, 'num_instance_available': num_instance_available,
         'num_authors': num_author,'num_genres': num_genre, 'book_title_contains':book_title}
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book