from pyexpat import model
from django import forms
from .models import Book, Category

class CategoreForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = ['name']
        wedgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }
    
def __str__(self):
    return self.title

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = [
             'title', 'auther', 'pages', 'retal_price_day', 'retal_period', 'active', 'status', 'category'
        ]
        wedgets = {
            'title'             : forms.TextInput(attrs={'class':'form-control', 'placeholder':'العنوان '}) ,
            'auther'            : forms.TextInput(attrs={'class':'form-control', 'placeholder':'المؤلف '}) ,
            # 'price'             : forms.TextInput(attrs={'class':'form-control', 'placeholder':'السعر '}) ,
            'photo_book'        : forms.TextInput(attrs={'class':'form-control', 'placeholder':'صورة الكتاب '}) ,
            'photo_auther'      : forms.TextInput(attrs={'class':'form-control', 'placeholder':'صورة المؤلف '}) ,
            'pages'             : forms.TextInput(attrs={'class':'form-control', 'placeholder':'الصفحات '}) ,
            'retal_price_day'   : forms.TextInput(attrs={'class':'form-control', 'placeholder':'سعر الإيجار لليوم  '}) ,
            'retal_period'      : forms.TextInput(attrs={'class':'form-control', 'placeholder':'سعر البيع '}) ,
            'active'            : forms.TextInput(attrs={'class':'form-control', 'placeholder':'الحالة '}) ,
            'category'          : forms.TextInput(attrs={'class':'form-control', 'placeholder':'التصنيف '}) ,
        }
        
def __str__(self):
    return self.title

