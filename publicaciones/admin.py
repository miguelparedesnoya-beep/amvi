from django.contrib import admin
from .models import FotoGaleria, Producto, Publicacion, InformacionNosotros


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "publicada", "fecha_creacion")
    list_filter = ("publicada", "fecha_creacion")
    search_fields = ("titulo", "descripcion")
    readonly_fields = ("fecha_creacion", "fecha_actualizacion")

    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponible", "fecha_creacion")
    list_filter = ("disponible",)
    search_fields = ("nombre", "descripcion")


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha_creacion")
    list_filter = ("categoria",)
    search_fields = ("titulo", "categoria")


@admin.register(InformacionNosotros)
class InformacionNosotrosAdmin(admin.ModelAdmin):
    list_display = ("__str__", "fecha_actualizacion")
    readonly_fields = ("fecha_actualizacion",)


admin.site.site_header = "AMVI — Administración"
admin.site.site_title = "AMVI Admin"
admin.site.index_title = "Panel administrativo"