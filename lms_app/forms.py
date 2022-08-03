from pyexpat import model
from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        
        
        