import csv
from django.http import HttpResponse
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *request, **queryset):
        response = HttpResponse(content_type='text/csv')
        #direction = request.GET.get('direction')
        #results = getattr(IpInfoDifference, direction)()
        response['Content-Disposition'] = 'attachment; filename="exportfile.csv"'
        writer = csv.writer(response)

        writer.writerow([u'longitude', u'latitude', u'ID', u'shift', u'date', u'age', u'primary_fur_color', u'location', u'running', u'chasing', u'climbing', u'eating', u'foraging', u'other_activities', u'kuks', u'quaas', u'moans', u'tail_flags', u'tail_twitches', u'approaches', u'indifferent', u'runs_from'])

        for item in queryset:
            writer.writerow(
                    [item[0],
                     item[1],
                     item[2],
                     item[3],
                     item[4],
                     item[5],
                     item[6],
                     item[7],
                     item[8],
                     item[9],
                     item[10],
                     item[11],
                     item[12],
                     item[13],
                     item[14],
                     item[15],
                     item[16],
                     item[17],
                     item[18],
                     item[19],
                     item[20],
                     item[21],
                     ]
            )
        return response

