from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.Charfield(max_lenth=50)
    
class Book(models.Model):
    title = models.Charfield(max_lenth=50)