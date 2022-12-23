from django.urls import path
from . import views

urlpatterns = [
   path('', views.home),
   path('list/', views.book_list),
   path('add/', views.book_create)
]