from django.contrib import admin
from catalogo.models import Autor, Genero, Idioma, Libro, Ejemplar

# Register your models here.

#admin.site.register(Autor)
#admin.site.register(Genero)
#admin.site.register(Idioma)
#admin.site.register(Libro)
#admin.site.register(Ejemplar)

#define la clase admin
class MyAutor(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fechaNac', 'fechaDeceso')
    list_filter = ('nombre', 'apellido', 'fechaNac', 'fechaDeceso')
#registra clase Admin junto al modelo base
admin.site.register(Autor, MyAutor)

class MyGenero(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
admin.site.register(Genero, MyGenero)

class MyIdioma(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
admin.site.register(Idioma, MyIdioma)

class MyLibro(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'resumen', 'isbn', 'muestra_genero')
    list_filter = ('titulo', 'autor', 'resumen', 'isbn', 'genero')
admin.site.register(Libro, MyLibro)

class MyEjemplar(admin.ModelAdmin):
    list_display = ('id', 'libro', 'fechaDeDevolucion', 'estado')
    list_filter = ('id', 'libro', 'fechaDeDevolucion', 'estado')
admin.site.register(Ejemplar, MyEjemplar)