from rest_framework import serializers
from .models import AuthorModel, CategoryModel, BookModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('f_name', 'l_name', 'date_of_birth', 'nationality')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('name', 'pub_date', 'description', 'author', 'category')