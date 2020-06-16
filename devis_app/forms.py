from django import forms

from .models import Devis, Emeteur, Client, GrillePrix

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = '__all__'


class EmetteurForm(forms.ModelForm):
    class Meta:
        model = Emeteur
        fields = ['nom', 'adresse', 'email', 'telephone', 'fax', 'SIRET', 'code_APE']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class GrillePrixForm(forms.ModelForm):
    class Meta:
        model = GrillePrix
        fields = '__all__'

