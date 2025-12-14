from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    nTelefono = models.CharField(max_length=15,blank=False)
    mensaje = models.TextField(blank=False)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length= 50, blank =False)
    emailCliente = models.EmailField(max_length=50)
    nTelefonoCliente = models.CharField(max_length=15,blank=False)
    fechaCliente = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombreCliente

class Suscripcion(models.Model):
    emailSus = models.EmailField(max_length=50, blank =False, unique=True)
    fechaSus = models.DateField(auto_now_add=True)
    estadoSus = models.BooleanField(default=True)

    def __str__(self):
        estado = "Activa" if self.estadoSus else "Inactiva"
        return f"{self.emailSus} - {estado}"
    

class Interes(models.Model):
    cliente = models.ForeignKey('main.Cliente', on_delete=models.CASCADE, related_name='intereses')
    propiedad = models.ForeignKey('manager.Propiedad', on_delete=models.CASCADE, related_name='intereses')
    creado = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.cliente} → {self.propiedad}"