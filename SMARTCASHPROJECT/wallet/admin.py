from django.contrib import admin
from .models import Categoria, Movimiento, Meta, EventoFijo, EventoPeriodico


admin.site.register(Categoria)
admin.site.register(Movimiento)
admin.site.register(Meta)
admin.site.register(EventoFijo)
admin.site.register(EventoPeriodico)
