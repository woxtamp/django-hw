import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=float(phone['price']),
                release_date=datetime.datetime.strptime(phone['release_date'], '%Y-%m-%d'),
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )
            new_phone.save()
