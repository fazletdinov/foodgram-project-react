import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import Ingredient

CSV_FILE = settings.BASE_DIR / 'data' / 'ingredients.csv'


class Command(BaseCommand):
    help = 'Загрузка ингридиентов'

    def handle(self, *args, **options):
        with open(CSV_FILE, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row)
                name = row['абрикосовое варенье']
                measurement_unit = row['г']
                Ingredient.objects.get_or_create(
                    name=name,
                    measurement_unit=measurement_unit,
                )
