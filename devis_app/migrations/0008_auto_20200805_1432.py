# Generated by Django 2.2.6 on 2020-08-05 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis_app', '0007_auto_20200728_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='date_creation',
            field=models.DateField(default=datetime.date.today, verbose_name=['%d/%m/%Y']),
        ),
        migrations.AlterField(
            model_name='devis',
            name='date_emission',
            field=models.DateField(blank=True, null=True, verbose_name=['%d/%m/%Y']),
        ),
        migrations.AlterField(
            model_name='devis',
            name='num_emission',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
