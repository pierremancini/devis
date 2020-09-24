from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth import get_user_model

class GrillePrix(models.Model):
    devise = models.CharField(max_length=200)
    total = models.FloatField(blank=True, null=True)

class Emeteur(models.Model):
    createur = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL, 
      null=True,
      blank=True
    )
    nom = models.CharField(max_length=500)
    adresse = models.TextField(blank=True)
    email = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)
    SIRET = models.CharField(max_length=200, blank=True)
    code_APE = models.CharField(max_length=200, blank=True)
    image_signature = models.ImageField(blank=True)

    # def __str__(self):
    #     return "Nom: {}, SIRET: {} n°id: {}".format(self.nom, self.code_APE, self.id)

class Client(models.Model):
    createur = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL, 
      null=True,
      blank=True
    )
    nom = models.CharField(max_length=500)
    adresse = models.TextField()
    email = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)

    # def __str__(self):
    #     return "{}, n°id {}".format(self.nom, self.id)


class Devis(models.Model):
    createur = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL, 
      null=True,
      blank=True
    )
    titre = models.CharField(max_length=200, default='Titre devis par défault')
    grille_prix = models.ForeignKey(GrillePrix, on_delete=models.CASCADE)
    emeteur = models.ForeignKey(Emeteur, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateField(blank= True, null=True)
    date_emission = models.DateField(blank=True, null=True)
    num_emission = models.SmallIntegerField(blank=True, null=False, default=0)
    # Text supplémentaire dans l'encadrer à gauche de l'affichage du prix total
    mention_total = models.CharField(max_length=100, blank=True, null=True)
    # Text juste avant la partie réservée à la signature
    mention = models.TextField(blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse('devis:detail', args=[self.id])


    # def __str__(self):
    #     return self.titre + " n°id " + self.id


class LignePrix(models.Model):
    grille_prix = models.ForeignKey(GrillePrix, on_delete=models.SET_NULL, null=True)
    designation = models.TextField(blank=True, null=True)
    quantité = models.IntegerField(default=1)
    prix_unit = models.FloatField()
    numero = models.IntegerField()
    montant = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "n°id: {},\ndesignation: {},\nquantité: {},\nprix_unit: {},\nnumero: {}".format(self.id, self.designation, self.quantité, self.prix_unit, self.numero)
