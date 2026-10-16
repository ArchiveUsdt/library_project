from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField("Автор", max_length=150)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="books", verbose_name="Категория")
    year = models.PositiveSmallIntegerField("Год издания")
    description = models.TextField("Описание", blank=True)
    cover = models.ImageField("Обложка", upload_to="covers/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.pk])
