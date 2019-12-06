from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
            help_text = _("Latitude of Squirrel"),
            max_length = 100,
    )


    longitude = models.FloatField(
            help_text = _("Longitudee of Squirrel"),
            max_length = 100,
    ) 

    unique_squirrel_ID = models.CharField(
            help_text = _("Unique Squirrel ID"),
            max_length = 100,
    )     

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = (
            (PM, 'PM'),
            (AM, 'AM'),
    )

    shift = models.CharField(
            help_text = _('Shift of Date'),
            max_length = 8,
            choices=SHIFT_CHOICES,
            default=AM
    )

    date = models.DateField(
            help_text=_('Date'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    NONE = ''

    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (NONE, 'None'),
    )

    age = models.CharField(
            help_text=_('Age'),
            max_length = 100,
            choices=AGE_CHOICES,
            default=NONE,
    )

    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    NONE = ''

    COLOR_CHOICES = (
            (BLACK, 'Black'),
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (NONE, 'None'),
    )

    primary_fur_color = models.CharField(
            help_text = _('Primary Color of Fur'),
            max_length = 100,
            choices=COLOR_CHOICES,
            default=NONE,
    )
    
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'
    NONE = ''

    LOCATION_CHOICES = (
            (GROUND, 'Ground Plane'),
            (ABOVE, 'Above Ground'),
            (NONE, 'None'),
    )

    location = models.CharField(
            help_text = _('Location'),
            max_length = 100,
            choices=LOCATION_CHOICES,
            default=NONE,
    )

    specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length = 100,
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
            help_text=_('Other Activities'),
            max_length = 100,
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


