from django.shortcuts import render
from django.http.response import HttpResponse
from hello.models import Book


def book_list(request):
    """書籍の一覧"""
    #return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request, 'hello/book_list.html', {'books': books})


def book_edit(request, book_id=None):
    """書籍の編集"""
    return HttpResponse('書籍の編集')


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')
