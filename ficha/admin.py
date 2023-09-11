from django.contrib import admin
from .models import *


class IdentificacionInmuebleAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'rol', 'unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'denominacion_inmueble', 'autor','usuario', 'created', 'updated')
    list_filter = ('unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'autor', 'created', 'updated')
    search_fields = ('id_plano', 'rol', 'unidad_vecinal', 'comuna', 'plan_cerro_poblacion', 'denominacion_inmueble', 'autor', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class PlanoUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'latitud', 'longitud', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'latitud', 'longitud', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class FotografiaGeneralAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class FotografiaContextoAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ResenaPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ValoracionAtributosAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class InformacionTecnicaAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class TipologiasAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class TipoCubiertaAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ElementosValorSignificativoAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ExpresionDeFachadaAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ContinuidadDeEdificacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class CaracteristicasMorfologicasAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class EstadoDeConservacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class GradoDeAlteracionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class AptitudDeRehabilitacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class RelacionDelInmuebleConElTerrenoAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class CategoriaDeAcuerdoASuUsoAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class ConclusionesAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

class FuentesReferencialesYBibliograficasAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')
class ObservacionAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('id_plano__id_plano', 'id_plano__rol', 'created', 'updated')
    ordering = ('id_plano', 'updated')
    readonly_fields = ('id_plano', 'created', 'updated')

admin.site.register(IdentificacionInmueble, IdentificacionInmuebleAdmin)
admin.site.register(PlanoUbicacion, PlanoUbicacionAdmin)
admin.site.register(FotografiaGeneral, FotografiaGeneralAdmin)
admin.site.register(FotografiaContexto, FotografiaContextoAdmin)
admin.site.register(ResenaPatrimonial, ResenaPatrimonialAdmin)
admin.site.register(ValoracionAtributos, ValoracionAtributosAdmin)
admin.site.register(InformacionTecnica, InformacionTecnicaAdmin)
admin.site.register(Tipologias, TipologiasAdmin)
admin.site.register(TipoCubierta, TipoCubiertaAdmin)
admin.site.register(ElementosValorSignificativo, ElementosValorSignificativoAdmin)
admin.site.register(ExpresionDeFachada, ExpresionDeFachadaAdmin)
admin.site.register(ContinuidadDeEdificacion, ContinuidadDeEdificacionAdmin)
admin.site.register(CaracteristicasMorfologicas, CaracteristicasMorfologicasAdmin)
admin.site.register(EstadoDeConservacion, EstadoDeConservacionAdmin)
admin.site.register(GradoDeAlteracion, GradoDeAlteracionAdmin)
admin.site.register(AptitudDeRehabilitacion, AptitudDeRehabilitacionAdmin)
admin.site.register(RelacionDelInmuebleConElTerreno, RelacionDelInmuebleConElTerrenoAdmin)
admin.site.register(CategoriaDeAcuerdoASuUso, CategoriaDeAcuerdoASuUsoAdmin)
admin.site.register(Conclusiones, ConclusionesAdmin)
admin.site.register(FuentesReferencialesYBibliograficas, FuentesReferencialesYBibliograficasAdmin)
admin.site.register(observacion, ObservacionAdmin)

