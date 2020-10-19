import tempfile
from django.template.loader import render_to_string
import subprocess
from django.http import HttpResponse
import os

def convert_to_pdf(html_content, header):
    """
    :param template: Chemin vers le template utilisé pour générer le HTML final
    :param header: HTML/String
    :param footer: HTML/String
    :param converter: Path to script returning pdf file content
    :return: Path du fichier pdf temporaire
    """

    tmp_html_path = '/tmp/tmp_out_facture.html'

    with open(tmp_html_path, 'w') as tmp_html:
        tmp_html.write(html_content)

    # Appel du script
    # node print-puppeteer.js --html "tmp_out_facture.html" 
    # --css "templates/devis.css" 
    # --pdf out_puppeteer.pdf 
    # --header "Facture n° 20200801"
    cmd = ['node', 'print-puppeteer.js',
        '--html', tmp_html_path, 
        '--css', 'templates/devis.css',
        '--pdf', '/tmp/tmp_out_puppeteer.pdf',
        '--header', header]

    # Récupérer le retour du script node.js sinon la page se charge sans arret
    foo = subprocess.call(cmd)
    pdf_path = '/tmp/tmp_out_puppeteer.pdf'

    os.remove(tmp_html_path)

    return pdf_path


def render_pdf_from_template(template, header, context):
    """ Fonction basée sur une fonction du même nom:
    https://github.com/namespace-ee/django-puppeteer-pdf/blob/master/puppeteer_pdf/utils.py
    
    A intégrer dans une view django.
    Remplace la fonction render (django.shortcuts).

    :param template: HTML template path
    :param header: 
    :param footer: 
    :return: 
    """

    # Render to string depuis le template: https://stackoverflow.com/questions/22162027/how-do-i-generate-a-static-html-file-from-a-django-template
    html_content = render_to_string(template, context)

    pdf_path = convert_to_pdf(html_content, header)

    # Servir le pdf:
    # https://ourcodeworld.com/articles/read/241/how-to-create-a-pdf-from-html-in-django
    # Create a URL of our project and go to the template route
    
    with open(pdf_path, 'rb') as pdf_file:

        # Generate download
        response = HttpResponse(pdf_file, content_type='application/pdf')

    os.remove(pdf_path)

    return response

