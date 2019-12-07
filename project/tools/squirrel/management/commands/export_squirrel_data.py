import csv
from django.http import HttpResponse
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Export Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        qs = Squirrel.objects.all()
        writer = csv.writer(open(path, 'w'), delimiter=',')

        headers = []
        for header in Squirrel._meta.get_fields():
            headers.append(header.name)
        writer.writerow(headers)

        for data in qs:
            row = []
            for header in headers:
                value = getattr(data, header)
                row.append(value)
            writer.writerow(row)
