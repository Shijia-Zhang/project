from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
            max_length = 100,
    )


    longitude = models.FloatField(
            max_length = 100,
    ) 

    ID = models.CharField(
            max_length = 100,
            primary_key = True,
    )     

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = (
            (PM, 'PM'),
            (AM, 'AM'),
    )

    shift = models.CharField(
            max_length = 8,
            choices=SHIFT_CHOICES,
            default=AM
    )

    date = models.DateField(
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
            max_length = 100,
            choices=AGE_CHOICES,
            blank=True
    )

    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'

    COLOR_CHOICES = (
            (BLACK, 'Black'),
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
    )

    primary_fur_color = models.CharField(
            max_length = 100,
            choices=COLOR_CHOICES,
            blank=True
    )
    
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    LOCATION_CHOICES = (
            (GROUND, 'Ground Plane'),
            (ABOVE, 'Above Ground'),
    )

    location = models.CharField(
            max_length = 100,
            choices=LOCATION_CHOICES,
            blank=True
    )

    specific_location = models.CharField(
            max_length = 100,
            blank=True
    )

    running = models.BooleanField(
            default=False)

    chasing = models.BooleanField(
            default=False)

    climbing = models.BooleanField(
            default=False)

    eating = models.BooleanField(
            default=False)

    foraging = models.BooleanField(
            default=False)

    other_activities = models.CharField(
            max_length = 100,
            blank = True
    )

    kuks = models.BooleanField(
            default=False)

    quaas = models.BooleanField(
            default=False)

    moans = models.BooleanField(
            default=False)

    tail_flags = models.BooleanField(
            default=False)

    tail_twitches = models.BooleanField(
            default=False)

    approaches = models.BooleanField(
            default=False)

    indifferent = models.BooleanField(
            default=False)

    runs_from = models.BooleanField(
            default=False)


