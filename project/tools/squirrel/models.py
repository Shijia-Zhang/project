from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
            max_length = 100,
    )


    longitude = models.FloatField(
            max_length = 100,
    ) 

    unique_squirrel_ID = models.CharField(
            max_length = 100,
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
            help_text = _('Running'),
            default=False)

    chasing = models.BooleanField(
            help_text = _('Chasing'),
            default=False)

    climbing = models.BooleanField(
            help_text = _('Climbing'),
            default=False)

    eating = models.BooleanField(
            help_text = _('Eating'),
            default=False)

    foraging = models.BooleanField(
            help_text = _('Foraging'),
            default=False)

    other_activities = models.CharField(
            max_length = 100,
            blank = True
    )

    kuks = models.BooleanField(
            help_text = _('Kuks'),
            default=False)

    quaas = models.BooleanField(
            help_text = _('Quaas'),
            default=False)

    moans = models.BooleanField(
            help_text = _('Moans'),
            default=False)

    tail_flags = models.BooleanField(
            help_text = _('Tail Flags'),
            default=False)

    tail_twitches = models.BooleanField(
            help_text = _('Tail Twitches'),
            default=False)

    approaches = models.BooleanField(
            help_text = _('Approaches'),
            default=False)

    indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            default=False)

    runs_from = models.BooleanField(
            help_text = _('Runs From'),
            default=False)


