from django.shortcuts import render, redirect
from .forms import BookCreationForm
from .models import Books
from django.utils import timezone

def index(request):
    books=Books.objects.all()
    print(books)
    return render(request, 'index.html', {'books': books})

def book_creation(request):
    if request.method == 'POST':
        form=BookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=BookCreationForm()
    return render(request, 'book_creation.html', {'form': form})

def book_detail(request, book_id):
    book = Books.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book':book})

def delete_book(request, book_id):
    book = Books.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'delete_book.html', {'book':book})

def update_book(request, book_id):
    book = Books.objects.get(id=book_id)
    print(book)
    form = BookCreationForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update_book.html', {'form':form})