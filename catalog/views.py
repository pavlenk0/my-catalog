from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_genres = Genre.objects.count()
    num_word = Book.objects.filter(title__contains='Harry').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available':
                 num_instances_available, 'num_authors': num_authors, 'num_genres': num_genres,
                 'num_word': num_word, 'num_visits': num_visits},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):

    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
