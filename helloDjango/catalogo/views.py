from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from catalogo.models import Idioma, Genero, Libro, Ejemplar, Autor
from django.views import generic
from catalogo.forms import GeneroForm, AutorForm, LibroForm, IdiomaForm

# Create your views here.
def catalogo(request):
    return render(request, 'catalogo.html', {})

def index(request):
    nroGeneros=Genero.objects.all().count()
    nroIdiomas=Idioma.objects.all().count()
    nroLibros=Libro.objects.all().count()
    nroEjemplares=Ejemplar.objects.all().count()
    nroDisponibles=Ejemplar.objects.filter(estado__exact='d').count()
    nroAutores=Autor.objects.count() #el 'all() esta implicito por defecto.'
    
    context = {
        'nroGeneros':nroGeneros,
        'nroIdiomas':nroIdiomas,
        'nroLibros':nroLibros,
        'nroEjemplares':nroEjemplares,
        'nroDisponibles':nroDisponibles,
        'nroAutores':nroAutores,
    }
    return render(request, 'catalogo.html', context)

class LibroListView(generic.ListView):
    model = Libro
    paginate_by = 2
    #context_object_name = 'libros'
    # en este caso va un modelo
    
    #queryset = Libro.objects.all()
    # si quiero filtrar
    
    template_name='libros.html'
    # nombre del template
    
    def get_context_data(self, **kwargs):
        libros = Libro.objects.all()
        context = super(LibroListView, self).get_context_data(**kwargs)
        context['libros'] = libros
        return context
    
class LibroDetailView(generic.DetailView):
    model = Libro
    template_name = 'libro.html'
    # Es obligatorio el nombre del template
    
    def libro_detail_view(request,pk):
        try:
            libro=Libro.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Oops! El libro no Existe")
        context = {
            'libro':libro,
        }
        return render(request, 'libro.html', context)
    
class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 2
    
    template_name='autores.html'
    
    def get_context_data(self, **kwargs):
        autores = Autor.objects.all()
        context = super(AutorListView, self).get_context_data(**kwargs)
        context['autores'] = autores
        return context

class AutorDetailView(generic.DetailView):
    model = Autor
    template_name = 'autor.html'
    
    def autor_detail_view(request,pk):
        try:
            autor=Autor.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Oops! El autor no existe")
        context = {
            'autor':autor,
        }
        return render(request, 'autor.html', context)
    
class GeneroListView(generic.ListView):
    model = Genero
    
    template_name='generos.html'
    
    def get_context_data(self, **kwargs):
        generos = Genero.objects.all()
        context = super(GeneroListView, self).get_context_data(**kwargs)
        context['generos'] = generos
        return context
    
class IdiomaListView(generic.ListView):
    model = Idioma
    
    template_name = 'idiomas.html'
    
    def get_context_data(self, **kwargs):
        idiomas = Idioma.objects.all()
        context = super(IdiomaListView, self).get_context_data(**kwargs)
        context['idiomas'] = idiomas
        return context
    
def genero_new(request):
    if request.method == "POST":
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.nombre = formulario.cleaned_data['nombre']
            genero.save()
            return redirect('generos')
    else:
        formulario = GeneroForm()
        
    return render(request, 'genero_new.html', {'formulario': formulario})

def genero_update(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    
    if request.method == "POST":
        formulario = GeneroForm(request.POST, instance=genero)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.nombre = formulario.cleaned_data['nombre']
            genero.save()
            return redirect('generos')
    else:
        formulario = GeneroForm(instance=genero)
        
    return render(request, 'genero_new.html', {'formulario': formulario})

def idioma_new(request):
    if request.method == "POST":
        formulario = IdiomaForm(request.POST)
        if formulario.is_valid():
            idioma = formulario.save(commit=False)
            idioma.nombre = formulario.cleaned_data['nombre']
            idioma.save()
            return redirect('idiomas')
    else:
        formulario = IdiomaForm()
        
    return render(request, 'idioma_new.html', {'formulario': formulario})
            
def idioma_update(request, pk):
    idioma = get_object_or_404(Idioma, pk=pk)
    
    if request.method == "POST":
        formulario = IdiomaForm(request.POST, instance=idioma)
        if formulario.is_valid():
            idioma = formulario.save(commit=False)
            idioma.nombre = formulario.cleaned_data['nombre']
            idioma.save()
            return redirect('idiomas')
    else:
        formulario = IdiomaForm(instance=idioma)
        
    return render(request, 'idioma_new.html', {'formulario': formulario})
        
def autor_new(request):
    if request.method == "POST":
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            autor = formulario.save(commit=False)
            autor.apellido = formulario.cleaned_data['apellido']
            autor.nombre = formulario.cleaned_data['nombre']
            autor.fechaNac = formulario.cleaned_data['fechaNac']
            autor.fechaDeceso = formulario.cleaned_data['fechaDeceso']
            autor.imagen = formulario.cleaned_data['imagen']
            autor.save()
            return redirect('autores')
    else:
        formulario = AutorForm()
    
    return render(request, 'autor_new.html', {'formulario': formulario})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    
    if request.method == "POST":
        formulario = AutorForm(request.POST, request.FILES)
        if formulario.is_valid():
            autor.apellido = formulario.cleaned_data['apellido']
            autor.nombre = formulario.cleaned_data['nombre']
            autor.fechaNac = formulario.cleaned_data['fechaNac']
            autor.fechaDeceso = formulario.cleaned_data['fechaDeceso']
            autor.imagen = formulario.cleaned_data['imagen']
            autor.save()
            return redirect('autores')
    else:
        formulario = AutorForm(instance=autor)
            
    return render(request, 'autor_new.html', {'formulario': formulario})
    
def libro_new(request):
    if request.method == "POST":
        formulario = LibroForm(request.POST, request.FILES)
        if formulario.is_valid():
            libro = formulario.save(commit=False)
            libro.titulo = formulario.cleaned_data['titulo']
            libro.autor = formulario.cleaned_data['autor']
            libro.resumen = formulario.cleaned_data['resumen']
            libro.isbn = formulario.cleaned_data['isbn']
            libro.genero = formulario.cleaned_data['genero']
            libro.imagen = formulario.cleaned_data['imagen']
            libro.save()
            return redirect('libros')
    else:
        formulario = LibroForm()
        
    return render(request, 'libro_new.html', {'formulario': formulario})

def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    
    if request.method == "POST":
        formulario = LibroForm(request.POST, request.FILES)
        if formulario.is_valid():
            libro.titulo = formulario.cleaned_data['titulo']
            libro.autor = formulario.cleaned_data['autor']
            libro.resumen = formulario.cleaned_data['resumen']
            libro.isbn = formulario.cleaned_data['isbn']
            libro.genero = formulario.cleaned_data['genero']
            libro.imagen = formulario.cleaned_data['imagen']
            libro.save()
            return redirect('libros')
    else:
        formulario = LibroForm(instance=libro)
        
    return render(request, 'libro_new.html', {'formulario': formulario})