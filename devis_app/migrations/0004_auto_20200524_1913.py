# Generated by Django 2.2.6 on 2020-05-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis_app', '0003_auto_20200520_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='emeteur',
            name='prenom',
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='nom',
            field=models.CharField(max_length=500),
        ),
    ]
