import tempfile
from django.template.loader import render_to_string
import subprocess
from django.http import HttpResponse
from django.http import FileResponse
from base64 import b64decode

def convert_to_pdf(content, header, footer):
    """
    :param template: Chemin vers le template utilisé pour générer le HTML final
    :param header: HTML/String
    :param footer: HTML/String
    :param converter: Path to script returning pdf file content
    :return: Fichier pdf
    """

    # Transforme le html/string en fichier temporaire
    html_tempfile = tempfile.NamedTemporaryFile()
    try:
        html_tempfile.write(content.encode('utf-8'))
        html_tempfile.flush()
    except:
        # Clean-up tempfile if an Exception is raised.
        html_tempfile.close()
        raise

    # Passer les argument au script node.js

    # Récupérer le retour du script node.js
    # 
    # node print-puppeteer.js --html "tmp_out_facture.html" 
    # --css "templates/devis.css" 
    # --pdf out_puppeteer.pdf 
    # --header "Facture n° 20200801"
    cmd = ['node', 'print-puppeteer.js',
        '--html', 'tmp_out_facture.html', 
        '--css', 'templates/devis.css',
        '--pdf', 'out_puppeteer.pdf',
        '--header','Facture n° 20200805']
    pdf_content = subprocess.call(cmd)

    return pdf_content

def render_pdf_from_template(template, header, footer, context):
    """ Fonction basée sur une fonction du même nom:
    https://github.com/namespace-ee/django-puppeteer-pdf/blob/master/puppeteer_pdf/utils.py
    
    A intégrer dans une view django.
    Remplace la fonction render (django.shortcuts).

    :param template: 
    :param header: 
    :param footer: 
    :return: 
    """

    # Render to string depuis le template: https://stackoverflow.com/questions/22162027/how-do-i-generate-a-static-html-file-from-a-django-template
    html_content = render_to_string(template, context)

    pdf_content = convert_to_pdf(html_content, header, footer)

    # Servir le pdf:
    # https://ourcodeworld.com/articles/read/241/how-to-create-a-pdf-from-html-in-django
    # Create a URL of our project and go to the template route

    print(pdf_content)
    pdf_content = pdf_content
    # print(pdf_content)

    # Generate download
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="devis.pdf"'

    return response

