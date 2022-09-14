from django.urls import  path
# from django.urls import urlpatterns, path
# from django.urls import URLPattern, path
from . import views


# URLPatterns = [
urlpatterns = [
    path('', views.index , name="index"),
    path('books', views.books , name="books"),
    path('update/<int:id>', views.update , name="update"),
    path('delete/<int:id>', views.delete , name="delete"),
]