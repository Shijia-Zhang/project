# Generated by Django 2.2.7 on 2019-12-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='name',
            field=models.CharField(default='pet', help_text='Names of pet', max_length=100),
            preserve_default=False,
        ),
    ]
