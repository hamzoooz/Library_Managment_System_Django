from django.db import models
   
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    # status_book = [
    #     ('availble', 'متاح'),
    #     ('rental', 'مستأجر'),
    #     ('sold', 'تم البيع'),
    # ]
    status_book = [
        ('availble', 'availble'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]
    
    title        = models.CharField(max_length=50)
    auther       = models.CharField(max_length=250, null=True, blank=True)
    shelf       = models.CharField(max_length=250, null=True, blank=True)
    locations       = models.CharField(max_length=250, null=True, blank=True)
    price        = models.DecimalField(max_digits=7 ,decimal_places=2, null=True, blank=True)
    photo_book   = models.ImageField(upload_to='photo', null=True, blank=True, default='/media/photo/photo1.png')
    photo_auther = models.ImageField(upload_to='photo', null=True, blank=True)
    pages        = models.IntegerField(null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=7 ,decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    active       = models.BooleanField(default=True)
    status       = models.CharField(max_length=50, choices = status_book,null=True, blank=True)
    category     = models.ForeignKey(Category, on_delete=models.PROTECT  , null=True, blank=True)
    
    number_of_rental = models.IntegerField(null=True, blank=True)
    number_of_download = models.IntegerField(null=True, blank=True)
    number_of_view = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title
