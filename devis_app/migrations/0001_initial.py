# Generated by Django 2.2.6 on 2020-05-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Emeteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('SIRET', models.CharField(max_length=200)),
                ('code_APE', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GrillePrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devise', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LignePrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200)),
                ('quantité', models.IntegerField(default=1)),
                ('prix_unit', models.FloatField()),
                ('grille_prix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devis_app.GrillePrix')),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateTimeField(verbose_name='date emission')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devis_app.Client')),
                ('emeteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devis_app.Emeteur')),
                ('grille_prix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devis_app.GrillePrix')),
            ],
        ),
    ]