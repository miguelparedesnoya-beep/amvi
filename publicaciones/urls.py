from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("productos/", views.productos, name="productos"),
    path("galeria/", views.galeria, name="galeria"),
    path("contacto/", views.contacto, name="contacto"),
    path("publicacion/<int:pk>/", views.detalle_publicacion, name="detalle_publicacion"),
]
