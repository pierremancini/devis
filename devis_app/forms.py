from django import forms

from .models import Devis, Emeteur, Client, GrillePrix

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = ['titre', 'date_creation', 'date_emission', 'num_emission']

class EmetteurForm(forms.ModelForm):
    class Meta:
        model = Emeteur
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class GrillePrixForm(forms.ModelForm):
    class Meta:
        model = GrillePrix
        fields = '__all__'

