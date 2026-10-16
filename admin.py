from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "year", "created_at")
    list_filter = ("category", "year")
    search_fields = ("title", "author__name")


admin.site.register(Author)
admin.site.register(Category)
