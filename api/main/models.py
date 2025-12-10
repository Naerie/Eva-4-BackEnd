from django.db import models
from django.utils.text import slugify

# Create your models here.
# tablas gestion
class TiposPropiedades(models.Model):
    tipoPropiedad = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.tipoPropiedad

class EstadosPropiedades(models.Model):
    estado = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.estado

class OperacionesPropiedades(models.Model):
    operacion = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.operacion

class Comunas(models.Model):
    comuna = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.comuna




class Propiedad(models.Model):
    MONEDAS = [
        ('UF', 'UF'),
        ('CLP', '$'),
    ]

    CANTIDADES = [(i, str(i)) for i in range(1, 11)] + [(11, '10+')]
    CANTIDADESEST = [(i, str(i)) for i in range(0, 11)] + [(11, '10+')]


    titulo = models.CharField(max_length=50, blank=False)
    thumb = models.ImageField(blank=False)
    descripcion = models.TextField()
    nHabitaciones = models.IntegerField(choices=CANTIDADES, default=1)
    nBanos = models.IntegerField(choices=CANTIDADES, default=1)
    superficie = models.FloatField(null=True, blank=True)
    superficieConstruida = models.FloatField(null=True, blank=True)
    ubicacion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    moneda = models.CharField(max_length=3, choices=MONEDAS, default='CLP')
    fecha = models.DateField(auto_now_add=True)
    # FK
    comuna = models.ForeignKey(
        Comunas,
        on_delete=models.PROTECT,
        null=True, 
        blank=True,
        related_name='propiedades',
        verbose_name='Comuna'
    )
    tipo_propiedad = models.ForeignKey(
        TiposPropiedades,
        on_delete=models.PROTECT,
        null=True, 
        blank=True,
        related_name='propiedades',
        verbose_name='Tipo de propiedad'
    )
    operacion = models.ForeignKey(
        OperacionesPropiedades,
        on_delete=models.PROTECT,
        null=True, 
        blank=True,
        related_name='propiedades',
        verbose_name='Operación'
    )
    estado = models.ForeignKey(
        EstadosPropiedades,
        on_delete=models.PROTECT,
        null=True, 
        blank=True,
        related_name='propiedades',
        verbose_name='Estado'
    )

    #EXTRAS
        #Depto
    conserje = models.BooleanField(default=False)
    logia = models.BooleanField(default=False)
    amoblado = models.BooleanField(default=False)
        #Ambos
    estacionamiento = models.BooleanField(default=False)
    nEstacionamientos = models.IntegerField(choices=CANTIDADESEST, default=0)
    piscina = models.BooleanField(default=False)
    # slug
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} - {self.precio} {self.moneda}"
    
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