from django import forms

from .models import Devis, Emeteur, Client, GrillePrix
from django.conf import settings

class DevisForm(forms.ModelForm):
    date_creation = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    date_emission = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    class Meta:
        model = Devis
        fields = ['titre', 'date_creation', 'date_emission', 'mention_total', 'mention']

FIELD_NAME_EMETTEUR = {
    'nom': 'nom_emetteur',
    'adresse': 'adresse_emetteur',
    'email':'email_emetteur',
    'telephone':'telephone_emetteur',
    'fax':'fax_emetteur'
}

class EmetteurForm(forms.ModelForm):
    class Meta:
        model = Emeteur
        fields = ['nom', 'adresse', 'email', 'telephone', 'fax', 'SIRET', 'code_APE', 'image_signature']

    # https://stackoverflow.com/questions/8801910/override-django-form-fields-name-attr
    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = FIELD_NAME_EMETTEUR.get(field_name, field_name)
        return super(EmetteurForm, self).add_prefix(field_name)


FIELD_NAME_CLIENT = {
    'nom': 'nom_client',
    'adresse': 'adresse_client',
    'email': 'email_client',
    'telephone': 'telephone_client',
    'fax': 'fax_client'
}


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ['nom', 'adresse', 'email', 'telephone', 'fax']

    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = FIELD_NAME_CLIENT.get(field_name, field_name)
        return super(ClientForm, self).add_prefix(field_name)


class GrillePrixForm(forms.ModelForm):
    class Meta:
        model = GrillePrix
        fields = '__all__'

