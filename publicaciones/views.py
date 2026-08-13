from django.shortcuts import get_object_or_404, render

from .models import FotoGaleria, Producto, Publicacion


WHATSAPP = "573142552654"


def inicio(request):
    publicaciones = Publicacion.objects.filter(
        publicada=True
    )[:6]

    productos = Producto.objects.filter(
        disponible=True
    )[:4]

    return render(
        request,
        "publicaciones/inicio.html",
        {
            "publicaciones": publicaciones,
            "productos": productos,
            "whatsapp": WHATSAPP,
        }
    )


def nosotros(request):
    return render(
        request,
        "publicaciones/nosotros.html"
    )


def productos(request):
    return render(
        request,
        "publicaciones/productos.html",
        {
            "productos": Producto.objects.filter(
                disponible=True
            ),
            "whatsapp": WHATSAPP,
        }
    )


def galeria(request):
    return render(
        request,
        "publicaciones/galeria.html",
        {
            "fotos": FotoGaleria.objects.all()
        }
    )


def contacto(request):
    return render(
        request,
        "publicaciones/contacto.html",
        {
            "whatsapp": WHATSAPP
        }
    )


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(
        Publicacion,
        pk=pk,
        publicada=True
    )

    return render(
        request,
        "publicaciones/detalle_publicacion.html",
        {
            "publicacion": publicacion
        }
    )
