from weasyprint import HTML, CSS

html = HTML(filename='devis_site_petit.html')
css = CSS(filename='devis.css')

html.write_pdf('devis_site_petit.pdf')