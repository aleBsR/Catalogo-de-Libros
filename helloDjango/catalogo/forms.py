from django import forms
from catalogo.models import Genero, Autor, Libro, Ejemplar, Idioma
from django.forms.widgets import NumberInput

class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = ('nombre',)
        
class IdiomaForm(forms.ModelForm):
    
    class Meta:
        model = Idioma
        fields = ('nombre',)
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('apellido', 'nombre', 'fechaNac', 'fechaDeceso', 'imagen')
        widgets = {
            'fechaNac': NumberInput(attrs={'type': 'date'}),
            'fechaDeceso': NumberInput(attrs={'type': 'date'}),
        }
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'autor', 'resumen', 'isbn', 'genero', 'imagen')

ESTADO_EJEMPLAR = (
        ('m', 'en mantenimiento'),
        ('p', 'prestado'),
        ('d', 'disponible'),
        ('r', 'reservado'),
    )
        
class EjemplarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].disbled = True
        
    estado = forms.ChoiceField(
        widget=forms.Select,
        choices=ESTADO_EJEMPLAR,
        initial='d'
    )
    
    class Meta:
        model = Ejemplar
        fields = ('id', 'libro', 'estado', 'fechaDeDevolucion')
        widgets = {
            'fechaDevolucion':NumberInput(attrs={'type':'date'}),
        }