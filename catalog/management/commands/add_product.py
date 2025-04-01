from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test productspython manage.py runserver to the database"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()

        products = [
            {
                "name": "Кефир",
                "description": "Кисломолочный продукт, созданнй по типу брожжения",
                "category": Category.objects.get(name="Молочные продукты"),
                "price": 150,
                "created_at": "2025-03-28",
                "updated_at": "2025-03-29",
            },
            {
                "name": "Ряженка",
                "description": "Кисломолочный продукт",
                "category": Category.objects.get(name="Молочные продукты"),
                "price": 80,
                "created_at": "2025-03-28",
                "updated_at": "2025-03-29",
            },
            {
                "name": "Йогурт",
                "description": "Ксиломолочный продукт",
                "category": Category.objects.get(name="Молочные продукты"),
                "price": 65,
                "created_at": "2025-03-28",
                "updated_at": "2025-03-29",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added student: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Student already exists: {product.name}"))
