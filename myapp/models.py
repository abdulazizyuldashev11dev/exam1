from django.db import models

class AuthorModel(models.Model):
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=150)


    def __str__(self):
        return f'{self.f_name} {self.l_name}'
class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BookModel(models.Model):
    name = models.CharField(max_length=300)
    pub_date = models.DateField()
    description = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
