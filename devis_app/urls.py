from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'devis'
urlpatterns = [
    # test
    path('list/', views.DevisList.as_view(), name='devis_list'),
    # exemple: /devis/ 
    path('', views.index, name='index'),
    # exemple: /devis/5/
    path('<int:devis_id>/', views.detail, name='detail'),
    # ex: /devis/5/preprint/
    path('<int:devis_id>/preprint/', views.preprint, name="preprint"),
    # exemple: /devis/nouveau/
    path('nouveau/', views.new, name="nouveau"),
    path('creer_devis/', views.new_devis, name="new_devis"),
    path('creer_emetteur/', views.new_emetteur, name="new_emetteur"),
    # ex: /devis/5/modifier/
    path('<int:devis_id>/modifier/', views.modifier, name="modifier")
    # Vues génériques
    # path('nouveau/', views.DevisCreate.as_view(), name='devis-add'),
]

