from weasyprint import HTML, CSS
import argparse
from jinja2 import Template
from datetime import date
import io

# Commande: python3 printer.py

parser = argparse.ArgumentParser(description="receuille les noms de fichiers pour construir le devis.")
parser.add_argument('--html', help='Nom et chemin de fichier html')
parser.add_argument('--css', help='Nom et chemin de fichier css')
parser.add_argument('--out', help='Nom et chemin du fichier de sortie')
args = parser.parse_args()

# Partie jinja
def num_devis():
    # on utilise os.walk, len
    return 12

# Passe le template sous forme d'objet fichier en memoire 
# et pas sous forme de nom de fichier à lire
with open(args.html, 'r') as file_object:

    # Modif jinja sur le file_object
    t = Template(file_object.read())
    fdate = date.today().strftime('%d/%m/%Y')
    # html = HTML(io.StringIO(t.render(num_devis=num_devis(), date=fdate)))
    html = HTML(string=t.render(num_devis=num_devis(), date=fdate))

css = CSS(filename=args.css)

html.write_pdf(args.out)