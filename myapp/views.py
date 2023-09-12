from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import AuthorModel, BookModel
from .serializers import AuthorSerializer, BookSerializer


# CRUD for AuthorModel
class AllAuthors(APIView):
    def get(self, request):
        all_data = AuthorModel.objects.all()
        serializer = AuthorSerializer(all_data, many=True)
        return Response(serializer.data)


class PostAuthor(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ChangeAuthor(APIView):
    def patch(self, request, *args, **kwargs):
        author = get_object_or_404(AuthorModel, id=kwargs['author_id'])
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class DeleteAuthor(APIView):
    def delete(self, request, *args, **kwargs):
        author = get_object_or_404(AuthorModel, id=kwargs['author_id'])
        author.delete()
        return Response({'msg': 'Succesfully DELETED'})


# CRUD for BookModel

class AllBooks(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class PostBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ChangeBook(APIView):
    def patch(self, request, *args, **kwargs):
        book = get_object_or_404(BookModel, id=kwargs['book_id'])
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteBook(APIView):
    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(BookModel, id=kwargs['book_id'])
        book.delete()
        return Response({'msg': 'Succesfully DELETED'})


class GetAuthorBook(APIView):
    def get(self, request, *args, **kwargs):
        author = get_object_or_404(AuthorModel, id=kwargs['aauthor_id'])
        books = BookModel.objects.filter(author=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)