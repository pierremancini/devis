import decimal

hebergement = {
    'grille': [
            {'designation': 'Location du serveur chez gandi.net' , 'quantité': 4, 'prix_unit': 1.1 },
            {'designation': 'Location du nom de domaine "labrouche.notaire.fr"',
                'quantité': 2,
                'prix_unit': 2.2 },
            {'designation': "Gestion du site, incluant: <br/> accès aux consoles, suivit du trafic, interventions d'urgences" ,
                'quantité': 1,
                'prix_unit': 1.1 },
        ],
    'devise': '€ / mois',
}

# calcul des montant/sous-totaux
for line in hebergement['grille']:
    line['montant'] = line['quantité'] * line['prix_unit']