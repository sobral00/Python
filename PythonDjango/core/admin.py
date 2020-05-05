from django.contrib import admin
from .models import (Marca,
                     Pessoa,
                     Veiculo,
                     Parametro,
                     MovRotativo,
                     Mensalista,
                     MovMensalista)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'checkin', 'checkout', 'valor_hora', 'horas_total', 'total', 'pago')


class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'inicio')


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total', 'pago')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovMensalista, MovMensalistaAdmin)


