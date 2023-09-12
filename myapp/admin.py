from django.contrib import admin
from .models import AuthorModel, CategoryModel, BookModel


admin.site.register(AuthorModel)
admin.site.register(CategoryModel)
admin.site.register(BookModel)