from django.urls import  path
# from django.urls import urlpatterns, path
# from django.urls import URLPattern, path
from . import views


# URLPatterns = [
urlpatterns = [
    path('', views.index , name="index"),
]