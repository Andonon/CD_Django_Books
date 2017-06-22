# -*- coding: utf-8 -*-
#pylint --disable=E1101
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Books
# Create your views here.
def index(request):
    Books.objects.create(title="Harry Potter and the Sorcerers Stone",
    author="J. K. Rowling",
    category="Children's", 
    published_date="1998-09-01 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Chamber of Secrets",
    author="J. K. Rowling",
    category="Children's", 
    published_date="1999-06-02 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Prisoner of Azkaban",
    author="J. K. Rowling",
    category="Children's", 
    published_date="1999-09-08 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Goblet of Fire",
    author="J. K. Rowling",
    category="Children's", 
    published_date="2000-07-08 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Order of the Phoenix",
    author="J. K. Rowling",
    category="Children's", 
    published_date="2003-06-21 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Half-Blood Prince",
    author="J. K. Rowling",
    category="Children's", 
    published_date="2005-07-16 00:00Z",
    in_print="True")
    Books.objects.create(title="Harry Potter and the Deathly Hallows",
    author="J. K. Rowling",
    category="Children's", 
    published_date="2007-07-21 00:00Z",
    in_print="True")
    books = Books.objects.all()
    print (books)
    return render(request, 'booksmodel/index.html')
