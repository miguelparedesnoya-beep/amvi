from django.conf import settings
from django.db import models
from django.urls import reverse


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to="publicaciones/",
        blank=True,
        null=True
    )

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="publicaciones_amvi",
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicada = models.BooleanField(default=True)

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("detalle_publicacion", args=[self.pk])


class Producto(models.Model):
    nombre = models.CharField(max_length=150)

    descripcion = models.TextField(
        blank=True
    )

    precio = models.DecimalField(
        max_digits=12,
        decimal_places=0
    )

    imagen = models.ImageField(
        upload_to="productos/",
        blank=True,
        null=True
    )

    disponible = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre


class FotoGaleria(models.Model):
    titulo = models.CharField(
        max_length=150,
        blank=True
    )

    imagen = models.ImageField(
        upload_to="galeria/"
    )

    categoria = models.CharField(
        max_length=100,
        default="Comunidad"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Foto de galería"
        verbose_name_plural = "Fotos de galería"

    def __str__(self):
        return self.titulo or f"Foto {self.pk}"


class InformacionNosotros(models.Model):
    historia = models.TextField(
        verbose_name="Historia de AMVI",
        help_text="Escribe aquí la historia de la asociación."
    )

    mision = models.TextField(
        verbose_name="Misión"
    )

    vision = models.TextField(
        verbose_name="Visión"
    )

    quienes_somos = models.TextField(
        verbose_name="Quiénes somos"
    )

    valores = models.TextField(
        verbose_name="Valores"
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Información de Nosotros"
        verbose_name_plural = "Información de Nosotros"

    def __str__(self):
        return "Información de AMVI"
