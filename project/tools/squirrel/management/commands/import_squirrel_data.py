import csv
import datetime
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
#change the name#

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data=list(reader)
        
        def boolean(x):
            if x == 'false':
                return False
            if x == 'true':
                return True

        for item in data:
            #change the name#
            p = Squirrel(
                latitude=item['X'],
                longitude=item['Y'],
                unique_squirrel_ID=item['Unique Squirrel ID'],
                shift=item['Shift'],
                date=datetime.date(int(str(item['Date'])[4:8]),int(str(item['Date'])[0:2]),int(str(item['Date'])[2:4])),
                age=item['Age'],
                primary_fur_color=item['Primary Fur Color'],
                location=item['Location'],
                running=boolean(item['Running']),
                chasing=boolean(item['Chasing']),
                climbing=boolean(item['Climbing']),
                eating=boolean(item['Eating']),
                foraging=boolean(item['Foraging']),
                other_activities=item['Other Activities'],
                kuks=boolean(item['Kuks']),
                quaas=boolean(item['Quaas']),
                moans=boolean(item['Moans']),
                tail_flags=boolean(item['Tail flags']),
                tail_twitches=boolean(item['Tail twitches']),
                approaches=boolean(item['Approaches']),
                indifferent=boolean(item['Indifferent']),
                runs_from=boolean(item['Runs from']),
            )
            p.save()

