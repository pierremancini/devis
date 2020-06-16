from django.db import models

class GrillePrix(models.Model):
    devise = models.CharField(max_length=200)

class Emeteur(models.Model):
    nom = models.CharField(max_length=500)
    adresse = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200, blank=True)
    SIRET = models.CharField(max_length=200)
    code_APE = models.CharField(max_length=200)

    def __str__(self):
        return "Nom: {}, SIRET: {} n°id: {}".format(self.nom, self.code_APE, self.id)

class Client(models.Model):
    nom = models.CharField(max_length=500)
    adresse = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "{}, n°id {}".format(self.nom, self.id)


class Devis(models.Model):
    titre = models.CharField(max_length=200, default='Titre devis par défault')
    grille_prix = models.ForeignKey(GrillePrix, on_delete=models.CASCADE)
    emeteur = models.ForeignKey(Emeteur, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateField('date creation', blank=True, null=True)
    date_emission = models.DateField('date emission', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('devis:detail', args=[self.id])


    def __str__(self):
        return self.title + " n°id " + self.id


class LignePrix(models.Model):
    grille_prix = models.ForeignKey(GrillePrix, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=200)
    quantité = models.IntegerField(default=1)
    prix_unit = models.FloatField()
