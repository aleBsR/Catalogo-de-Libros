from django.db import models
from django.urls import reverse
import uuid #requerida para la instancia de libros unicos

# Create your models here.

class Genero(models.Model):
    """
    Modelo que representa un genero literario
    """
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del gènero")
    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    """
    Modelo que representa un idioma
    """
    nombre = models.CharField(max_length=50, help_text="ingrese un idioma")
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    """
    Modelo que representa un autor
    """
    nombre = models.CharField(max_length=50, help_text="ingrese el nombre")
    apellido = models.CharField(max_length=50, help_text="ingrese el apellido")
    fechaNac = models.DateField(null=True, blank=True)
    fechaDeceso = models.DateField('Fallecido', null=True, blank=True)
    imagen = models.ImageField(upload_to='media/autor', null=True)
    
    def get_absolute_url(self):
        """
        devuelve la url para acceder a un autor
        """
        return reverse('autorInfo', args=[str(self.id)])
    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)
    class Meta:
        ordering = ["apellido", "nombre"]
    
class Libro(models.Model):
    """
    Modelo que representa un libro
    """
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    #uso ForeignKey, ya que un libro tiene un solo autor, pero un mismo autor puede haber escrito muchos libros
    resumen = models.CharField(max_length=1000, help_text="ingrese un resumen del libro")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genero = models.ManyToManyField(Genero, help_text="seleccione un genero (o varios) para el libro")
    #ManyToManyField, porque un genero puede contener muchos libros y un libro puede cubrir varios generos
    #la clase genero ya fue definida, entonces podemos especificar el objeto arriba
    imagen = models.ImageField(upload_to='media/libro', null=True)
    
    def muestra_genero(self):
        return ', '.join([ genero.nombre for genero in self.genero.all()[:3]])
    
    muestra_genero.short_description = 'Genero/s'
    
    def get_absolute_url(self):
        return reverse('LibroInfo', args=[str(self.id)])
    
    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ["titulo",]


class Ejemplar(models.Model):
    """
    modelo que representa un ejemplar de un libro
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para este libro particular en toda la biblioteca")
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    fechaDeDevolucion = models.DateField(null=True, blank=True)
    
    ESTADO_EJEMPLAR = (
        ('m', 'en mantenimiento'),
        ('p', 'prestado'),
        ('d', 'disponible'),
        ('r', 'reservado'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='d', help_text='Disponibilidad del ejemplar')
    
    class Meta:
        ordering = ["fechaDeDevolucion"]
    
    def __str__(self):
        return '%s (%s)' % (self.id, self.libro.titulo)
    
    def tituloEstado(self):
        return '(%s)' % (self.get_estado_display())