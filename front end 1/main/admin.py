from django.contrib import admin
from main.models import Contacto, Cliente, Suscripcion

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 
                    'email', 
                    'nTelefono', 
                    'mensaje', 
                    'fecha']
    readonly_fields = [
        'nombre',
        'email',
        'nTelefono',
        'mensaje',
        'fecha'
        ]
    list_filter = [ 
        'fecha',
        ]
    list_per_page = 10

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombreCliente',
                    'emailCliente',
                    'nTelefonoCliente',
                    'fechaCliente']
    readonly_fields = [
        'fechaCliente'
        ]
    list_filter = [ 
        'fechaCliente',
        ]
    list_per_page = 10

    
class SusAdmin(admin.ModelAdmin):
    list_display = ['emailSus',
                    'fechaSus',
                    'estadoSus']
    readonly_fields = [
        'emailSus',
        'fechaSus'
        ]
    list_filter = [ 
        'fechaSus',
        ]
    list_per_page = 10

    
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Suscripcion, SusAdmin)
