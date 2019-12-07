# Generated by Django 2.2.7 on 2019-12-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(blank=True, help_text='Other Activities', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], help_text='Primary Color of Fur', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(blank=True, help_text='Specific Location', max_length=100),
        ),
    ]