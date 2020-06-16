from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Devis, Emeteur
from .forms import DevisForm, EmetteurForm, ClientForm, GrillePrixForm


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
        form = DevisForm(request.POST)
        new_devis = ''
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
    return HttpResponse("Modifications du devis n° %s, bientot disponibles" % devis_id)



# ------ Test des vues génériques ---------
class DevisList(ListView):
    model = Devis
