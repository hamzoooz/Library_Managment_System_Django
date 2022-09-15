from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import BookForm,CategoreForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            
    add_category = CategoreForm(request.POST)
    if add_category.is_valid():
        add_category.save()
        
    context = {
        'category': Category.objects.all(),
        'books':    Book.objects.all(),
        'form' :    BookForm(),
        'catform':  CategoreForm(),
        'allbook': Book.objects.filter(active=True).count(),
        'bookslid': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailble': Book.objects.filter(status='available').count(),
        # 'bookslid': Book.objects.filter(status='تم البيع').count(),
        # 'bookrental': Book.objects.filter(status='مستأجر').count(),
        # 'bookavailble': Book.objects.filter(status='متاح').count(),
    }
    return render(request, 'pages/index.html', context)
 
def books(request):
    context = {
    'category': Category.objects.all(),
    'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)        
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else : 
        book_save = BookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context )

def delete(request,id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method=='POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')