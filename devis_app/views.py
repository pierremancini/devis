from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.contrib import messages

from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Devis, Emeteur, Client, GrillePrix, LignePrix
from .forms import DevisForm, EmetteurForm, ClientForm, GrillePrixForm

from pprint import pprint
import re
from datetime import datetime

def index(request):
    try:
        dernier_crees = Devis.objects.order_by('-date_creation')[:9]
        dernier_emis = Devis.objects.exclude(date_emission=None).order_by('-date_emission')[:9]
    except Devis.DoesNotExist:
        raise Http404("Devis n° {} inexistant".format(devis_id))
    return render(request, 'devis_app/index.html', {'dernier_crees': dernier_crees,
        'dernier_emis': dernier_emis})

def detail(request, devis_id):
    try:
        devis = Devis.objects.get(pk=devis_id)
    except Devis.DoesNotExist:
        raise Http404("Devis n° {} inexistant".format(devis_id))
    return render(request, 'devis_app/detail.jinja', {'devis': devis})

def preprint(request, devis_id):
    try:
        # On passe tout les valeurs nécessaires à la création du pdf
        # Pour cela on utilise l'identifiant du devis et on remonte aux autres valeurs qui lui sont liées
        devis = Devis.objects.get(pk=devis_id)
        grille = devis.grille_prix
        lignes = grille.ligneprix_set.all
        emeteur = devis.emeteur
        client = devis.client
    except Devis.DoesNotExist:
        raise Http404("Devis n° {} inexistant".format(devis_id))
    return render(request, 'devis_app/print_devis.jinja',
        {
            'devis': devis,
            'emeteur': emeteur,
            'client': client,
            'grille': grille,
            'lines': lignes
        })

# Les vues Create/Update
def new(request):
    if request.method == 'GET':
        form_devis = DevisForm()
        form_emetteur = EmetteurForm()
        form_client = ClientForm()
        form_grille = GrillePrixForm()
    elif request.method == 'POST':
        form_devis = DevisForm(request.POST)
        form_emetteur = EmetteurForm(request.POST)
        form_client = ClientForm(request.POST)
        form_grille = GrillePrixForm(request.POST)

        new_client = Client(
            nom = request.POST['nom_client'],
            adresse = request.POST['adresse_client'],
            email = request.POST['email_client'],
            telephone = request.POST['telephone_client'],
            fax = request.POST['fax_client']
        )

        new_emetteur = Emeteur(
            nom = request.POST['nom_emetteur'],
            adresse = request.POST['adresse_emetteur'],
            email = request.POST['email_emetteur'],
            telephone = request.POST['telephone_emetteur'],
            fax = request.POST['fax_emetteur'],
            SIRET = request.POST['SIRET'],
            code_APE = request.POST['code_APE'],
            image_signature = request.POST['image_signature']
        )

        new_grille = GrillePrix(
            devise = request.POST['devise']
        )

        new_client.save()
        new_emetteur.save()
        new_grille.save()

        if request.POST['date_creation']:
            date_creation = datetime.strptime(request.POST['date_creation'], '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            date_creation = None

        if  request.POST['date_emission']:
            date_emission = atetime.strptime(request.POST['date_emission'], '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            date_emission = None

        new_devis = Devis(
            titre = request.POST['titre'],
            emeteur = new_emetteur,
            client = new_client,
            grille_prix = new_grille,
            date_creation = date_creation,
            date_emission = date_emission,
            num_emission = request.POST['num_emission'],
            mention_total = request.POST['mention_total'],
            mention = request.POST['mention'])

        pprint(new_devis)

        new_devis.save()

        # Instanciation des objects ligne
        lines = {}
        for i in request.POST:
            if re.match('^(l\d+)_(.*)$', i):
                m = re.match('^l(\d+)_(.*)$', i)
                line_num = m.group(1)
                lines.setdefault(line_num, {})
                field = m.group(2)
                if field == 'designation':
                    lines[line_num]['designation'] = request.POST[i]
                elif field == 'quantity':
                    lines[line_num]['quantity'] = request.POST[i]
                elif field == 'prix-unite':
                    lines[line_num]['prix-unite'] = request.POST[i].replace(',', '.')

        for n in lines:
            ligne_prix = LignePrix(
                grille_prix = new_grille,
                designation = lines[n]['designation'],
                quantité = lines[n]['quantity'],
                prix_unit = lines[n]['prix-unite']
            )

            ligne_prix.save()

    return render(request, 'devis_app/tabs_new.jinja', 
        {'devis': form_devis, 
        'emetteur': form_emetteur,
        'client': form_client,
        'grille': form_grille})

def new_devis(request):
    if request.method == 'GET':
        form = DevisForm()
    elif request.method == 'POST':
        form = DevisForm(request.POST)
        new_devis = ''
    return render(request, 'devis_app/new_object.jinja', {'view': form, 'type': 'Devis'})

def new_emetteur(request):
    if request.method == 'GET':
        form = EmetteurForm()
    elif request.method == 'POST':
        form = EmetteurForm(request.POST)
        new_emetteur = Emeteur(
            nom = request.POST['nom'],
            adresse = request.POST['adresse'],
            email = request.POST['email'],
            telephone = request.POST['telephone'],
            fax = request.POST['fax'],
            SIRET = request.POST['SIRET'],
            code_APE = request.POST['code_APE']
        )
        new_emetteur.save()
        return HttpResponseRedirect(reverse('devis:index'))
    return render(request, 'devis_app/new_object.jinja', {'view': form, 'type': 'Emetteur'})

def new_client(request):
    if request.method == 'GET':
        form = ClientForm()
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        new_emetteur = ''
    return render(request, 'devis_app/new_object.jinja', {'view': form, 'type': 'Client'})

def modifier(request, devis_id):
    if request.method == 'GET':
        devis = Devis.objects.get(pk=devis_id)

        # Récupérer les objects liés à devis

        form_devis = DevisForm(instance=devis)
        form_emetteur = EmetteurForm(instance=devis.emeteur)
        form_client = ClientForm(instance=devis.client)
        form_grille = GrillePrixForm(instance=devis.grille_prix)

        lines = devis.grille_prix.ligneprix_set.all()

    elif request.method == 'POST':
        devis = Devis.objects.get(pk=devis_id)

        # Récupérer les objects liés à devis
        form_devis = DevisForm(instance=devis)
        form_emetteur = EmetteurForm(instance=devis.emeteur)
        form_client = ClientForm(instance=devis.client)
        form_grille = GrillePrixForm(instance=devis.grille_prix)

        lines = devis.grille_prix.ligneprix_set.all()

        client = Client(
            nom = request.POST['nom_client'],
            adresse = request.POST['adresse_client'],
            email = request.POST['email_client'],
            telephone = request.POST['telephone_client'],
            fax = request.POST['fax_client']
        )

        emetteur = Emeteur(
            nom = request.POST['nom_emetteur'],
            adresse = request.POST['adresse_emetteur'],
            email = request.POST['email_emetteur'],
            telephone = request.POST['telephone_emetteur'],
            fax = request.POST['fax_emetteur'],
            SIRET = request.POST['SIRET'],
            code_APE = request.POST['code_APE'],
            image_signature = request.POST['image_signature']
        )

        grille = GrillePrix(
            devise = request.POST['devise']
        )

        client.save()
        emetteur.save()
        grille.save()

        devis = Devis(
            titre = request.POST['titre'],
            emeteur = emetteur,
            client = client,
            grille_prix = grille,
            date_creation = request.POST['date_creation'],
            date_emission = request.POST['date_emission'],
            num_emission = request.POST['num_emission'],
            mention_total = request.POST['mention_total'],
            mention = request.POST['mention'])

        devis.save()

        # Instanciation des objects ligne
        lines = {}
        for i in request.POST:
            if re.match('^(l\d+)_(.*)$', i):
                m = re.match('^l(\d+)_(.*)$', i)
                line_num = m.group(1)
                lines.setdefault(line_num, {})
                field = m.group(2)
                if field == 'designation':
                    lines[line_num]['designation'] = request.POST[i]
                elif field == 'quantity':
                    lines[line_num]['quantity'] = request.POST[i]
                elif field == 'prix-unite':
                    lines[line_num]['prix-unite'] = request.POST[i].replace(',', '.')

        # A changer, on doit modifier certaines lignes au lieu d'instancier de nouveaux objets
        for n in lines:
            ligne_prix = LignePrix(
                grille_prix = new_grille,
                designation = lines[n]['designation'],
                quantité = lines[n]['quantity'],
                prix_unit = lines[n]['prix-unite']
            )

            ligne_prix.save()



    return render(request, 'devis_app/modifier.jinja', 
        {'devis': form_devis, 
        'emetteur': form_emetteur,
        'client': form_client,
        'grille': form_grille,
        'lines': lines})


def delete(request, devis_id):
    devis = Devis.objects.get(pk=devis_id)
    devis.delete()
    return redirect('/devis')

# ------ Test des vues génériques ---------
class DevisList(ListView):
    model = Devis
