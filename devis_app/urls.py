from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from puppeteer_pdf.views import PDFTemplateView

from . import views

app_name = 'devis'
urlpatterns = [
    # test
    path('list_emetteur_client/', views.list_emetteur_client, name='list_emetteur_client'),
    # exemple: /devis/ 
    path('', views.index, name='index'),
    # exemple: /devis/5/
    path('<int:devis_id>/', views.preprint, name='detail'),
    # ex: /devis/5/preprint/
    path('<int:devis_id>/preprint/', views.preprint, name="preprint"),
    # exemple: /devis/nouveau/
    path('nouveau/', views.new, name="nouveau"),
    path('creer_devis/', views.new_devis, name="new_devis"),
    path('creer_emetteur/', views.new_emetteur, name="new_emetteur"),
    path('creer_client/', views.new_client, name="new_client"),
    # ex: /devis/5/modifier/
    path('<int:devis_id>/modifier/', views.modifier, name="modifier"),
    path('<int:devis_id>/delete/', views.delete, name='delete'),
    path('<int:emetteur_id>/delete_emetteur/', views.delete_emetteur, name='delete_emetteur'),
    path('<int:client_id>/delete_client/', views.delete_client, name='delete_client'),
    # Vues génériques
    # path('nouveau/', views.DevisCreate.as_view(), name='devis-add'),
    # Génration du pdf
    # path('<int:devis_id>/pdf/', PDFTemplateView.as_view(template_name='devis_app/pdf.html', filename='devis.pdf'), name='pdf')
    path('<int:devis_id>/pdf/', views.pdf, name='pdf')
]

