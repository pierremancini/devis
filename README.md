# Présentation

- Les ojectifs de ce projet était de:

1/ Génération de document en .pdf à partir de fichiers .html et .css. Utilise pupeteer et chronium pour générer le .pdf avec une bonne gestion des en-tête, numérotation des pages et respect du .css.
2/ Apprendre à utiliser le framework Django.

- L'application utilise le system d'authenfication de django pour permettre aux utilisateurs de gérer les devis indépendement de ce que font les autres utilisateurs.

- Les données des devis sont enregistrées dans une base SQLite et sont structurées en entité-relation pour permettre une utilistation dans différents contextes plus facile (par exemple réutiliser le données liées à un client pour faire un nouveau devis).


# Installation

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

1/ `mkdir devis && chmod 755 -R devis && chown mancini:www-data devis && cd devis`
2/ `virtualenv devisenv && source devisenv/bin/activate`
3/ `pip3 install gunicorn && pip3 install -r requirements.txt`
4/ `cd /etc && mkdir devis && cd devis && nano django_secret_key.txt && chown mancini:www-data django_secret_key.txt && chmod 640 django_secret_key.txt`
5/ Ne pas utiliser `python manage.py makemigrations` https://stackoverflow.com/a/42548860/3759545 mais seulement `python manage.py migrate`
6/`python manage.py createsuperuser`
7/ `nano /etc/systemd/system/devis.service`
8/ `systemctl start devis && systemctl enable devis`
9/ `nano /etc/nginx/sites-available/pierremancini`
10/ `systemctl restart nginx`