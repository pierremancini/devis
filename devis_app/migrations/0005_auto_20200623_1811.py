# Generated by Django 2.2.6 on 2020-06-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis_app', '0004_auto_20200524_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='mention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='mention_total',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='num_emission',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emeteur',
            name='image_signature',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='adresse',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='SIRET',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='adresse',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='code_APE',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='emeteur',
            name='telephone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ligneprix',
            name='designation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
