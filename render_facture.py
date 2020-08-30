import argparse
from jinja2 import Template
from datetime import date
import io
import prix
import emeteur
import client

# Commande pour facture: python3 render_facture.py --jinja templates/facture_debut_site.jinja --out tmp_out_facture.html

parser = argparse.ArgumentParser(description="receuille les noms de fichiers pour construir le devis.")
parser.add_argument('--jinja', help='Nom et chemin du template')
parser.add_argument('--out', help='Nom et chemin du fichier de sortie')
args = parser.parse_args()

def num_facture():
    date_part = date.today().strftime('%Y%m')

    # Incrémentation automatique à implémenter dans la future app/django
    num_du_mois = "01"

    return date_part + num_du_mois

fdate = date.today().strftime('%d/%m/%Y')
titre = "Facture n°"

template_var = {
    'num_facture': num_facture(),
    'date_reglement': '31/08/2020',
    'date_prestation': '10/05/2020',
    'titre': titre,
    'nom_emeteur': emeteur.nom,
    'adresse_emeteur': emeteur.adresse,
    'email_emeteur': emeteur.email,
    'telephone_emeteur': emeteur.telephone,
    'SIRET_emeteur': emeteur.SIRET,
    'Code_APE_emeteur': emeteur.Code_APE,
    'nom_client': client.nom,
    'adresse_client': client.adresse,
    'telephone_client': client.telephone,
    'fax_client': client.fax,
    'email_client': client.email,
}

# Passe le template sous forme d'objet fichier en memoire 
# et pas sous forme de nom de fichier à lire
with open(args.jinja, 'r') as jinja_file, open(args.out, 'w') as html_file:

    # Modif jinja sur le file_object
    t = Template(jinja_file.read())
    # html = HTML(io.StringIO(t.render(num_devis=num_devis(), date=fdate)))
    string_html = t.render(**template_var)

    html_file.write(string_html)
