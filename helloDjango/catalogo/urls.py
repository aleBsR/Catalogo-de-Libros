from django.urls import path
from catalogo import views

urlpatterns = [
    #path('', views.catalogo, name='catalogo'),
    path('', views.index, name='index'),
    path('libros/', views.LibroListView.as_view(), name='libros'),
    path('libro/<pk>', views.LibroDetailView.as_view(), name='libro'),
    path('libro/new/', views.libro_new, name='libro_new'),
    path('libro/update/<pk>', views.libro_update, name='libro_update'),
    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('autor/<pk>', views.AutorDetailView.as_view(), name='autor'),
    path('autor/new/', views.autor_new, name='autor_new'),
    path('autor/update/<pk>', views.autor_update, name='autor_update'),
    path('generos/', views.GeneroListView.as_view(), name='generos'),
    path('genero/new/', views.genero_new, name='genero_new'),
    path('genero/update/<pk>', views.genero_update, name='genero_update'),
]
