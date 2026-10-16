from datetime import date

from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "category", "year", "description", "cover"]
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 2:
            raise forms.ValidationError("Название должно содержать минимум 2 символа.")
        return title

    def clean_year(self):
        year, current = self.cleaned_data["year"], date.today().year
        if not 1000 <= year <= current:
            raise forms.ValidationError(f"Укажите год от 1000 до {current}.")
        return year

    def clean_cover(self):
        cover = self.cleaned_data.get("cover")
        if cover and hasattr(cover, "size") and cover.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Файл обложки не должен превышать 2 МБ.")
        return cover
