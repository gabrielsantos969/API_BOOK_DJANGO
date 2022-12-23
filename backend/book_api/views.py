from django.shortcuts import render
from rest_framework.response import Response
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    data = {
        "recepcao": "Bem vindo a api de livros!",
        "author": "Gabriel Santos"
    }
    return Response(data)

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)