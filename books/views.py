from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView

from books.models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
