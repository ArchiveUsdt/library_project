import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Категория")),
            ],
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Автор")),
            ],
            options={"verbose_name": "Автор", "verbose_name_plural": "Авторы", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("year", models.PositiveSmallIntegerField(verbose_name="Год издания")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("cover", models.ImageField(blank=True, upload_to="covers/", verbose_name="Обложка")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="books",
                                             to="library.author", verbose_name="Автор")),
                ("category", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               related_name="books", to="library.category", verbose_name="Категория")),
            ],
            options={"verbose_name": "Книга", "verbose_name_plural": "Книги", "ordering": ["-created_at"]},
        ),
    ]
