from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book, Category

SORTS = {"new": "-created_at", "title": "title", "year": "-year"}


def filter_books(params):
    """Поиск по названию/автору (без учёта регистра, в т.ч. кириллицы), фильтр по категории, сортировка."""
    qs = Book.objects.select_related("author", "category")
    category = params.get("category", "")
    if category.isdigit():
        qs = qs.filter(category_id=category)
    books = list(qs.order_by(SORTS.get(params.get("sort"), "-created_at")))
    q = params.get("q", "").strip().casefold()
    if q:
        books = [b for b in books if q in b.title.casefold() or q in b.author.name.casefold()]
    return books


def home(request):
    return render(request, "library/home.html", {
        "latest": Book.objects.select_related("author", "category")[:3],
        "total": Book.objects.count(),
    })


def book_list(request):
    return render(request, "library/book_list.html", {
        "books": filter_books(request.GET),
        "categories": Category.objects.all(),
        "params": request.GET,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book.objects.select_related("author", "category"), pk=pk)
    return render(request, "library/book_detail.html", {"book": book})


def book_edit(request, pk=None):
    """Создание (pk=None) и редактирование книги: GET показывает форму, POST сохраняет."""
    book = get_object_or_404(Book, pk=pk) if pk else None
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if request.method == "POST":
        if form.is_valid():
            book = form.save()
            messages.success(request, "Книга сохранена.")
            return redirect(book)
        messages.error(request, "Исправьте ошибки в форме.")
    return render(request, "library/book_form.html", {"form": form, "book": book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Книга удалена.")
        return redirect("book_list")
    return redirect(book)


def contacts(request):
    return render(request, "library/contacts.html")


# ---------- API ----------
def _error(message, status):
    return JsonResponse({"error": message}, status=status, json_dumps_params={"ensure_ascii": False})


def _book_json(request, b):
    return {
        "id": b.id, "title": b.title, "author": b.author.name,
        "category": b.category.name if b.category else None,
        "year": b.year, "description": b.description,
        "cover": request.build_absolute_uri(b.cover.url) if b.cover else None,
    }


def api_books(request):
    if request.method != "GET":
        return _error("Метод не поддерживается, используйте GET.", 405)
    category, sort = request.GET.get("category", ""), request.GET.get("sort")
    if category and not category.isdigit():
        return _error("Параметр category должен быть числом.", 400)
    if sort and sort not in SORTS:
        return _error("Параметр sort: new, title или year.", 400)
    books = filter_books(request.GET)
    return JsonResponse({"count": len(books), "results": [_book_json(request, b) for b in books]},
                        json_dumps_params={"ensure_ascii": False})


def api_book_detail(request, pk):
    if request.method != "GET":
        return _error("Метод не поддерживается, используйте GET.", 405)
    book = Book.objects.select_related("author", "category").filter(pk=pk).first()
    if book is None:
        return _error("Книга не найдена.", 404)
    return JsonResponse(_book_json(request, book), json_dumps_params={"ensure_ascii": False})
