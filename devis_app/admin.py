from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(GrillePrix)
admin.site.register(Emeteur)
admin.site.register(Client)
admin.site.register(Devis)
admin.site.register(LignePrix)
