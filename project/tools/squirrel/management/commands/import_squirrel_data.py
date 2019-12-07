import csv
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
#change the name#

class Command(BaseCommand):
    def add_argument(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data=list(reader)

        for item in data:
            #change the name#
            p = Squirrel(
                latitude=item['X'],
                longitude=item['Y'],
                unique_squirrel_ID=item['Unique Squirrel ID'],
                shift=item['Shift'],
                date=item['Date'],
                age=item['Age'],
                primary_fur_color=item['Primary Fur Color'],
                location=item['Location'],
                running=item['Running'],
                chasing=item['Chasing'],
                climbing=item['Climbing'],
                eating=item['Eating'],
                foraging=item['Foraging'],
                other_activities=item['Other Activities'],
                kuks=item['Kuks'],
                quaas=item['Quaas'],
                moans=item['Moans'],
                tail_tags=item['Tail tags'],
                tail_twitches=item['Tail twitches'],
                approaches=item['Approaches'],
                indifferent=item['Indifferent'],
                runs_from=item['Runs from'],
            )
            p.save()

