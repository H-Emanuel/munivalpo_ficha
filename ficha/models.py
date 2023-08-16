from django.db import models
import os
from auditlog.registry import auditlog
from django.contrib.auth.models import User

REGION_CHOICES = [
    ('VALPARAÍSO', 'Valparaíso'),
]

COMUNA_CHOICES = [
    ('VALPARAÍSO', 'Valparaíso'),
    ('LAGUNA VERDE', 'Laguna Verde'),
    ('PLACILLA', 'Placilla'),
    ('PLAYA ANCHA', 'Playa Ancha'),
]

PLAN_CERRO_POBLACION = [
    ('PLAN', 'Plan'),
    ('CERRO', 'Cerro'),
    ('POBLACION', 'Poblacion'),
]

# Sección 1
class IdentificacionInmueble(models.Model):
    id_plano = models.BigAutoField(primary_key=True, unique=True)
    
    rol = models.CharField(max_length=100, blank=True, default='00000-00000')
    unidad_vecinal = models.CharField(max_length=255, blank=True, default='')
    region = models.CharField(max_length=50, choices=REGION_CHOICES, default='VALPARAÍSO')
    comuna = models.CharField(max_length=50, choices=COMUNA_CHOICES, default='VALPARAÍSO')
    calle = models.CharField(max_length=255, blank=True, default='')
    numero = models.CharField(max_length=50, blank=True, default='')
    plan_cerro_poblacion = models.CharField(max_length=255, blank=True,choices=PLAN_CERRO_POBLACION, default='PLAN')
    denominacion_inmueble = models.CharField(max_length=255, blank=True, default='')
    autor = models.CharField(max_length=255, blank=True, default='Se desconoce')
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "identificacion_inmueble"
        verbose_name_plural = "identificaciones_inmuebles"

    def __int__(self):
        return int (self.id_plano) +1 

    def __str__(self):
        return str(self.id_plano) + ' - ' + self.rol  
    
# Sección 2
def content_file_name_plano(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('p', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

class PlanoUbicacion(models.Model):
    # imagen_plano = models.ImageField(upload_to="plano_ubicacion", blank=True, default='')
    imagen_plano = models.ImageField(upload_to=content_file_name_plano, blank=True, default='',null=True)
    latitud = models.CharField(max_length=100, blank=True, default='')
    longitud = models.CharField(max_length=100, blank=True, default='')
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "plano_ubicacion"
        verbose_name_plural = "planos_ubicaciones"

# Sección 3
def content_file_name_general(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('g', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

class FotografiaGeneral(models.Model):
    imagen_fotografia = models.ImageField(upload_to=content_file_name_general, blank=True, default='')
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "fotografia_general"
        verbose_name_plural = "fotografias_generales"

# Sección 4
def content_file_name_contexto_1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('c1', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_contexto_2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('c2', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

class FotografiaContexto(models.Model):
    registro_fotografico_1 = models.ImageField(upload_to=content_file_name_contexto_1, blank=True, default='')
    registro_fotografico_2 = models.ImageField(upload_to=content_file_name_contexto_2, blank=True, default='')
    fecha_registro_fotografico = models.DateField(auto_now=True)
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "fotografia_contexto"
        verbose_name_plural = "fotografias_contextos"

# Sección 5
class ResenaPatrimonial(models.Model):
    valor_urbano = models.TextField(blank=True, default='')
    valor_arquitecnico = models.TextField(blank=True, default='')
    valor_historico = models.TextField(blank=True, default='')
    valor_economico = models.TextField(blank=True, default='')
    valor_social = models.TextField(blank=True, default='')
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "resena_patrimonial"
        verbose_name_plural = "resenas_patrimoniales"

# Sección 6
class ValoracionAtributos(models.Model):
    valor_urbano_a = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_urbano_b = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_urbano_c = models.PositiveSmallIntegerField(default=0, blank=True)

    valor_arquitecnico_a = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_arquitecnico_b = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_arquitecnico_c = models.PositiveSmallIntegerField(default=0, blank=True)

    valor_historico_a = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_historico_b = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_historico_c = models.PositiveSmallIntegerField(default=0, blank=True)

    valor_economico_a = models.PositiveSmallIntegerField(default=0, blank=True)
    valor_economico_b = models.PositiveSmallIntegerField(default=0, blank=True)

    valor_social_a = models.PositiveSmallIntegerField(default=0, blank=True)
    
    valor_resumen  = models.PositiveSmallIntegerField(default=0, blank=True)
    zona_de_conservacion = models.CharField(max_length=255, blank=True, default='')
    identificacion_zch = models.CharField(max_length=100, blank=True, default='')
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "valoracion_atributos"
        verbose_name_plural = "valoraciones_atributos"

# Sección 7
PERIODOS_CONSTRUCCION = [
    ('ANTERIOR A 1900', 'Anterior a 1900'),
    ('1901-1920', '1901-1920'),
    ('1921-1940', '1921-1940'),
    ('1941-1960', '1941-1960'),
    ('1961-1970', '1961-1970'),
    ('1971-1990', '1971-1990'),
    ('POST 1990', 'Post 1990'),
]

TIPO_PROPIEDAD = [
    ('PARTICULAR', 'Particular'),
    ('FISCAL', 'Fiscal'),
    ('MUNICIPAL', 'Municipal'),
]

TIPO_DESTINO_INMUEBLE = [
    ('', ''),
    ('1 - VIVIENDA', '1 - Vivienda'),
    ('2 - COMERCIO', '2 - Comercio'),
    ('3 - SERVICIO', '3 - Servicio'),
    ('4 - EDUCACION', '4 - Educacion'),
    ('5 - SALUD', '5 - Salud'),
    ('6 - DEPORTE', '6 - Deporte'),
    ('7 - RECREACION', '7 - Recreacion'),
    ('8 - CULTURA', '8 - Cultura'),
    ('9 - CULTO', '9 - Culto'),
    ('10 - INDUSTRIA', '10 - Industria'),
    ('11 - BODEGA', '11 - Bodega'),
]

TIPO_USUARIO = [
    ('PROPIETARIO', 'Propietario'),
    ('ARRENDATARIO', 'Arrendatario'),
    ('USUFRUCTUARIO', 'Usufructuario'),
]

REGIMEN_PROPIEDAD = [
    ('INDIVIDUAL', [
        ('PERSONA NATURAL', 'Persona Natural'),
        ('PERSONA JURIDICA', 'Persona Jurídica'),
    ]),
    ('COLECTIVA', [
        ('COMUNIDAD', 'Comunidad'),
        ('SUCESION', 'Sucesión'),
    ]),
]

AFECTACION_ACTUAL = [
    ('DECLARACION DE UTILIDAD PUBLICA', 'Declaración de Utilidad Pública'),
    ('ANTEJARDIN', 'Antejardín'),
]

class InformacionTecnica(models.Model):
    piso_original_subterraneo = models.CharField(max_length=255,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA',blank=True,)
    piso_original_primer_piso = models.CharField(max_length=255, blank=True,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA')
    piso_original_pisos_superiores = models.CharField(max_length=255, blank=True,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA')
    piso_actual_subterraneo = models.CharField(max_length=255, blank=True,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA')
    piso_actual_primer_piso = models.CharField(max_length=255, blank=True,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA')
    piso_actual_pisos_superiores = models.CharField(max_length=255, blank=True,choices=TIPO_DESTINO_INMUEBLE, default='VIVIENDA')

    anio_construccion = models.CharField(max_length=50, choices=PERIODOS_CONSTRUCCION, default='ANTERIOR A 1900', blank=True)

    tipo_propiedad = models.CharField(max_length=50, choices=TIPO_PROPIEDAD, default='PARTICULAR', blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='PROPIETARIO', blank=True)

    regimen_propiedad = models.CharField(max_length=50, choices=REGIMEN_PROPIEDAD, default='INDIVIDUAL', blank=True)

    afectacion_actual = models.CharField(max_length=50, choices=AFECTACION_ACTUAL, default='DECLARACION DE UTILIDAD PUBLICA', blank=True)

    observaciones = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "informacion_tecnica"
        verbose_name_plural = "informaciones_tecnicas"

# Sección 8
SISTEMA_AGRUPAMIENTO = [
    ('AISLADO', 'Aislado'),
    ('PAREADO', 'Pareado'),
    ('CONTINUO', 'Continuo'),
    ('AISLADO SOBRE CONTINUIDAD', 'Aislado sobre continuidad'),
]

VOLUMETRIA = [
    ('SIMPLE', 'Simple'),
    ('COMPLEJA', 'Compleja'),
    ('MIXTA', 'Mixta'),
]

MATERIALIDAD_ESTRUCTURA = [
    ('ACERO', 'Acero'),
    ('HORMIGON ARMADO', 'Hormigón Armado'),
    ('ALBAÑILERIA', 'Albañilería'),
    ('PIEDRA', 'Piedra'),
    ('MADERA', 'Madera'),
    ('ADOBE', 'Adobe'),
]

MATERIALIDAD_CUBIERTA = [
    ('FIBROCEMENTO', 'Fibrocemento'),
    ('TEJAS', 'Tejas'),
    ('TEJUELA (ZINC)', 'Tejuela (Zinc)'),
    ('ACERO GALVANIZADO', 'Acero Galvanizado'),
]
MATERIALIDAD_REVESTIMIENTO = [
    ('ENLUCIDO/ESTUCO', 'Enlucido/estuco'),
    ('MADERA', 'Madera'),
    ('PLACHA TOLENADA', 'Placha tolenada'),
    ('HORMIGON ', 'Hormigo a la vista'),
    ('OTRO', 'Otro'),
]

class Tipologias(models.Model):
    manzana = models.BooleanField(default=False)
    esquina = models.BooleanField(default=False)
    entre_medianeros = models.BooleanField(default=False)
    cabezal = models.BooleanField(default=False)
    crucero = models.BooleanField(default=False)
    doble_frente = models.BooleanField(default=False)
    antejardines = models.BooleanField(default=False)

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tipologia"
        verbose_name_plural = "tipologias"
class TipoCubierta(models.Model):
    horizontal = models.BooleanField(default=False)
    inclinada = models.BooleanField(default=False)
    curva = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    otro_texto = models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tipo_cubierta"
        verbose_name_plural = "tipos_cubiertas"

class ElementosValorSignificativo(models.Model):
    cornisamientos = models.BooleanField(default=False)
    zocalos = models.BooleanField(default=False)
    molduras_relevantes_en_yeso = models.BooleanField(default=False)
    ornamentacion_en_madera = models.BooleanField(default=False)
    remate_en_techumbre = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    otro_texto = models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "elemento_valor_significativo"
        verbose_name_plural = "elementos_valores_significativos"

class ExpresionDeFachada(models.Model):
    lenguaje_de_vanos_comun = models.BooleanField(default=False)
    simetria = models.BooleanField(default=False)
    modulacion_en_serie = models.BooleanField(default=False)
    torreon_en_esquina = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    otro_texto = models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "expresion_de_fachada"
        verbose_name_plural = "expresiones_de_fachadas"

class ContinuidadDeEdificacion(models.Model):
    fachada = models.BooleanField(default=False)
    linea_de_remate_superior = models.BooleanField(default=False)
    linea_de_zocalo_escalonado = models.BooleanField(default=False)
    linea_de_zocalo_continuo = models.BooleanField(default=False)
    realce_horizontal_prodominante = models.BooleanField(default=False)
    zocalo_de_mamposteria = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    otro_texto = models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "continuidad_de_edificacion"
        verbose_name_plural = "continuidades_de_edificaciones"

def content_file_name_significativo(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_1', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_fachada(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_2', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_constructivos(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_3', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_contexto_1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_4', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_contexto_2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_5', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

def content_file_name_contexto_3(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('detalle_6', ext)
    folder = "assets_ficha/" + str(instance.id_plano.id_plano)
    return os.path.join(folder, filename)

class CaracteristicasMorfologicas(models.Model):
    tipologia = models.ForeignKey(Tipologias, on_delete=models.CASCADE)
    sistema_agrupamiento = models.CharField(max_length=50, choices=SISTEMA_AGRUPAMIENTO, default='AISLADO', blank=True)
    tipo_cubierta = models.ForeignKey(TipoCubierta, on_delete=models.CASCADE)
    volumetria = models.CharField(max_length=50, choices=VOLUMETRIA, default='SIMPLE', blank=True)
    elementos_valor_significativo = models.ForeignKey(ElementosValorSignificativo, on_delete=models.CASCADE)
    expresion_de_fachada = models.ForeignKey(ExpresionDeFachada, on_delete=models.CASCADE)
    continuidad_de_edificacion = models.ForeignKey(ContinuidadDeEdificacion, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, default='')

    fotografia_valor_significativo = models.ImageField(upload_to=content_file_name_significativo, blank=True, null=True)
    fotografia_expresion_fachada = models.ImageField(upload_to=content_file_name_fachada, blank=True, null=True)
    fotografia_detalles_constructivos = models.ImageField(upload_to=content_file_name_constructivos, blank=True, null=True)

    fotografia_contexto_1 = models.ImageField(upload_to=content_file_name_contexto_1, blank=True, null=True)
    fotografia_contexto_2 = models.ImageField(upload_to=content_file_name_contexto_2, blank=True, null=True)
    fotografia_contexto_3 = models.ImageField(upload_to=content_file_name_contexto_3, blank=True, null=True)


    terreno = models.FloatField(default=0, blank=True)
    edificada = models.FloatField(default=0, blank=True)
    protegida = models.FloatField(default=0, blank=True)
    altura_en_pisos = models.FloatField(default=0, blank=True)
    altura_en_metros = models.FloatField(default=0, blank=True)
    antejardin_frente_1 = models.FloatField(default=0, blank=True)
    antejardin_frente_2 = models.FloatField(default=0, blank=True)

    materialidad_estructura = models.CharField(max_length=50, choices=MATERIALIDAD_ESTRUCTURA, default='ACERO', blank=True)
    materialidad_cubierta = models.CharField(max_length=50, choices=MATERIALIDAD_CUBIERTA, default='ACERO', blank=True)
    materialidad_revestimientos = models.CharField(max_length=255,choices= MATERIALIDAD_REVESTIMIENTO, default='ENLUCIDO/ESTUCO', blank=True)

    descripcion_del_inmubebles= models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "caracteristica_morfologica"
        verbose_name_plural = "caracteristicas_morfologicas"

# Sección 9
ESTADO_CONSERVACION = [
    ('BUENO', 'Bueno'),
    ('REGULAR', 'Regular'),
    ('MALO', 'Malo'),
]

class EstadoDeConservacion(models.Model):
    inmueble = models.CharField(max_length=50, choices=ESTADO_CONSERVACION, default='BUENO', blank=True)
    entorno = models.CharField(max_length=50, choices=ESTADO_CONSERVACION, default='BUENO', blank=True)

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "estado_de_conservacion"
        verbose_name_plural = "estados_de_conservacion"
    
# Sección 10
GRADO_ALTERACION = [
    ('SIN MODIFICACION', 'Sin modificacion'),
    ('POCO MODIFICADO', 'Poco modificado'),
    ('MUY MODIFICADO', 'Muy modificado'),
]

class GradoDeAlteracion(models.Model):
    fachada = models.CharField(max_length=50, choices=GRADO_ALTERACION, default='SIN MODIFICACION', blank=True)
    cubierta = models.CharField(max_length=50, choices=GRADO_ALTERACION, default='SIN MODIFICACION', blank=True)

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "grado_de_alteracion"
        verbose_name_plural = "grados_de_alteracion"

# Sección 11
class AptitudDeRehabilitacion(models.Model):
    vivienda = models.BooleanField(default=False)
    equipamiento = models.BooleanField(default=False)
    comercio = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)
    otro_texto = models.CharField(max_length=255, blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "aptitud_de_rehabilitacion"
        verbose_name_plural = "aptitudes_de_rehabilitacion"

# Sección 12
ESPACIO_PUBLICO = [
    ('COLINDA', 'Colinda'),
    ('ENFRENTA', 'Enfrenta'),
]

INMUEBLES_PATRIMONIALES = [
    ('PREDIO CONTIGUO', 'Predio contiguo'),
    ('MANZANA', 'Manzana'),
    ('MANZANA ENFRENTE', 'Manzana enfrente'),
    ('RELACION VISUAL', 'Relacion visual'),
]

PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL = [
    ('PLACA EN FACHADA', 'Placa en fachada'),
    ('ESCULTURA', 'Escultura'),
    ('MONUMENTOS PUBLICOS', 'Monumentos publicos'),
    ('RELACION VISUAL', 'Relacion visual'),
]

class RelacionDelInmuebleConElTerreno(models.Model):
    imagen_urbana_relevante_por_ubicacion = models.BooleanField(default=False)
    imagen_urbana_relevante_por_singularidad = models.BooleanField(default=False)

    forma_parte_de_un_conjunto = models.BooleanField(default=False)

    espacio_publico = models.CharField(max_length=50, choices=ESPACIO_PUBLICO, default='COLINDA', blank=True)

    # No usar
    monumentos_historicos = models.CharField(max_length=50, choices=INMUEBLES_PATRIMONIALES, default='PREDIO CONTIGUO', blank=True)
    inmuebles_conservacion_historica = models.CharField(max_length=50, choices=INMUEBLES_PATRIMONIALES, default='PREDIO CONTIGUO', blank=True)

    mon_his_predio_contiguo = models.BooleanField(default=False)
    mon_his_manzana = models.BooleanField(default=False)
    mon_his_manzana_enfrente = models.BooleanField(default=False)
    mon_his_relacion_visual = models.BooleanField(default=False)

    inm_con_his_predio_contiguo = models.BooleanField(default=False)
    inm_con_his_manzana = models.BooleanField(default=False)
    inm_con_his_manzana_enfrente = models.BooleanField(default=False)
    inm_con_his_relacion_visual = models.BooleanField(default=False)
    Otros_elementos_patrimonial = models.TextField(blank=True, default='PLACA EN FACHADA',choices=PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL)
    observaciones = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "relacion_del_inmueble_con_el_terreno"
        verbose_name_plural = "relaciones_de_inmueble_con_el_terreno"

# Sección 13
class CategoriaDeAcuerdoASuUso(models.Model):
    observaciones = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoria_de_acuerdo_a_su_uso"
        verbose_name_plural = "categorias_de_acuerdo_a_su_uso"

# Sección 14
class Conclusiones(models.Model):
    conclusiones = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "conclusiones"
        verbose_name_plural = "conclusiones"

# Sección 15
class FuentesReferencialesYBibliograficas(models.Model):
    fuentes_referenciales_y_bibliograficas = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "fuentes_referenciales_y_bibliograficas"
        verbose_name_plural = "fuentes_referenciales_y_bibliograficas"

# Sección Extras
class Verificacion(models.Model):
    aprobado = models.BooleanField(blank=True, default=False)
    aprobado_revisor = models.BooleanField(blank=True, default=False)
    observacion = models.TextField(blank=True ,default="")


    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    usuario_trabajador = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    usuario_revisor = models.TextField(blank=True ,default="")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "verificacion"
        verbose_name_plural = "verificaciones"



auditlog.register(IdentificacionInmueble)
auditlog.register(PlanoUbicacion)
auditlog.register(FotografiaGeneral)
auditlog.register(FotografiaContexto)
auditlog.register(ResenaPatrimonial)
auditlog.register(ValoracionAtributos)
auditlog.register(InformacionTecnica)
auditlog.register(Tipologias)
auditlog.register(TipoCubierta)
auditlog.register(ElementosValorSignificativo)
auditlog.register(ExpresionDeFachada)
auditlog.register(ContinuidadDeEdificacion)
auditlog.register(CaracteristicasMorfologicas)
auditlog.register(EstadoDeConservacion)
auditlog.register(GradoDeAlteracion)
auditlog.register(AptitudDeRehabilitacion)
auditlog.register(RelacionDelInmuebleConElTerreno)
auditlog.register(CategoriaDeAcuerdoASuUso)
auditlog.register(Conclusiones)
auditlog.register(FuentesReferencialesYBibliograficas)
