from django.core.management.base import BaseCommand

from library.models import Author, Book, Category

DATA = [
    ("Война и мир", "Лев Толстой", "Роман", 1869, "Роман-эпопея о русском обществе в эпоху наполеоновских войн."),
    ("Преступление и наказание", "Фёдор Достоевский", "Роман", 1866, "История студента Раскольникова и цены, которую платят за идею."),
    ("Герой нашего времени", "Михаил Лермонтов", "Роман", 1840, "Психологический роман о Печорине."),
    ("Мёртвые души", "Николай Гоголь", "Поэма", 1842, "Путешествие Чичикова по русской провинции."),
    ("Евгений Онегин", "Александр Пушкин", "Поэма", 1833, "Роман в стихах — энциклопедия русской жизни."),
    ("Вишнёвый сад", "Антон Чехов", "Драма", 1904, "Пьеса о разорении дворянского гнезда."),
]


class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными"

    def handle(self, *args, **options):
        for title, author, category, year, text in DATA:
            a, _ = Author.objects.get_or_create(name=author)
            c, _ = Category.objects.get_or_create(name=category)
            Book.objects.get_or_create(title=title, author=a, defaults={"category": c, "year": year, "description": text})
        self.stdout.write(self.style.SUCCESS(f"Книг в базе: {Book.objects.count()}"))
