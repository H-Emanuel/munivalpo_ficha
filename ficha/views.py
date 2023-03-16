from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings

from .helpers import save_pdf, save_pdf_2
from datetime import datetime
from datetime import date


# Create your views here.
def ficha_home(request):
    # identificacion_inmueble = IdentificacionInmueble.objects.all()
    # plano_ubicacion = PlanoUbicacion.objects.all()
    # fotografia_general = FotografiaGeneral.objects.all()
    # resena_patrimonial = ResenaPatrimonial.objects.all()
    # valoracion_atributos = ValoracionAtributos.objects.all()

    data = {}
    return render(request, 'ficha/home.html', data)

@login_required(login_url='/login/')
def crear_ficha(request):
    last_id =  IdentificacionInmueble.objects.latest('id_plano')
    # TRANFORMAR EL ULTIMO ID DE STRING A NUMERICO
    identificacion_inmueble = IdentificacionInmueble.objects.create(id_plano = last_id)
    plano_ubicacion = PlanoUbicacion.objects.create(id_plano_id = last_id)
    fotografia_general = FotografiaGeneral.objects.create(id_plano_id = last_id)
    fotografia_contexto = FotografiaContexto.objects.create(id_plano_id = last_id)
    resena_patrimonial = ResenaPatrimonial.objects.create(id_plano_id = last_id)
    valoracion_atributos = ValoracionAtributos.objects.create(id_plano_id = last_id)
    informacion_tecnica = InformacionTecnica.objects.create(id_plano_id = last_id)
    estado_de_conservacion = EstadoDeConservacion.objects.create(id_plano_id = last_id)
    grado_de_alteracion = GradoDeAlteracion.objects.create(id_plano_id = last_id)
    aptitud_de_rehabilitacion = AptitudDeRehabilitacion.objects.create(id_plano_id = last_id)
    relacion_del_inmueble_con_el_terreno = RelacionDelInmuebleConElTerreno.objects.create(id_plano_id = last_id)
    categoria_de_acuerdo_a_su_uso = CategoriaDeAcuerdoASuUso.objects.create(id_plano_id = last_id)
    conclusiones = Conclusiones.objects.create(id_plano_id = last_id)
    fuentes_referenciales_y_bibliograficas = FuentesReferencialesYBibliograficas.objects.create(id_plano_id = last_id)

    tipologia = Tipologias.objects.create(id_plano_id = last_id)
    tipo_cubierta = TipoCubierta.objects.create(id_plano_id = last_id)
    elementos_valor_significativo = ElementosValorSignificativo.objects.create(id_plano_id = last_id)
    expresion_fachada = ExpresionDeFachada.objects.create(id_plano_id = last_id)
    continuidad_edificacion = ContinuidadDeEdificacion.objects.create(id_plano_id = last_id)
    obj1 = Tipologias.objects.latest('id')
    obj2 = TipoCubierta.objects.latest('id')
    obj3 = ElementosValorSignificativo.objects.latest('id')
    obj4 = ExpresionDeFachada.objects.latest('id')
    obj5 = ContinuidadDeEdificacion.objects.latest('id')

    caracteristicas_morfologicas = CaracteristicasMorfologicas.objects.create(id_plano_id = last_id,
                                                                              tipologia = obj1,
                                                                              tipo_cubierta = obj2,
                                                                              elementos_valor_significativo = obj3,
                                                                              expresion_de_fachada = obj4,
                                                                              continuidad_de_edificacion = obj5)

    OPTIONS = {
        'PLAN_CERRO_POBLACION': PLAN_CERRO_POBLACION,
        'REGION_CHOICES': REGION_CHOICES,
        'COMUNA_CHOICES': COMUNA_CHOICES,
        'PERIODOS_CONSTRUCCION': PERIODOS_CONSTRUCCION,
        'TIPO_DESTINO_INMUEBLE': TIPO_DESTINO_INMUEBLE,
        'TIPO_PROPIEDAD': TIPO_PROPIEDAD,
        'TIPO_USUARIO': TIPO_USUARIO,
        'REGIMEN_PROPIEDAD': REGIMEN_PROPIEDAD,
        'AFECTACION_ACTUAL': AFECTACION_ACTUAL,
        'SISTEMA_AGRUPAMIENTO': SISTEMA_AGRUPAMIENTO,
        'VOLUMETRIA': VOLUMETRIA,
        'MATERIALIDAD_ESTRUCTURA': MATERIALIDAD_ESTRUCTURA,
        'MATERIALIDAD_CUBIERTA': MATERIALIDAD_CUBIERTA,
        'SISTEMA_AGRUPAMIENTO': SISTEMA_AGRUPAMIENTO,
        'VOLUMETRIA': VOLUMETRIA,
        'MATERIALIDAD_ESTRUCTURA': MATERIALIDAD_ESTRUCTURA,
        'MATERIALIDAD_CUBIERTA': MATERIALIDAD_CUBIERTA,
        'ESTADO_CONSERVACION': ESTADO_CONSERVACION,
        'GRADO_ALTERACION': GRADO_ALTERACION,
        'ESPACIO_PUBLICO': ESPACIO_PUBLICO,
        'INMUEBLES_PATRIMONIALES': INMUEBLES_PATRIMONIALES,
        'PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL': PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL,
        'MATERIALIDAD_REVESTIMIENTO': MATERIALIDAD_REVESTIMIENTO,
    }

    # Sección 6
    total_valor_urbano = valoracion_atributos.valor_urbano_a + valoracion_atributos.valor_urbano_b + valoracion_atributos.valor_urbano_c
    total_valor_arquitecnico = valoracion_atributos.valor_arquitecnico_a + valoracion_atributos.valor_arquitecnico_b + valoracion_atributos.valor_arquitecnico_c
    total_valor_historico = valoracion_atributos.valor_historico_a + valoracion_atributos.valor_historico_b
    total_valor_economico_social = valoracion_atributos.valor_economico_social_a + valoracion_atributos.valor_economico_social_b + valoracion_atributos.valor_economico_social_c
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico_social

    if request.method == 'POST':
        # Sección 1
        identificacion_inmueble.rol = request.POST.get('rol')
        identificacion_inmueble.unidad_vecinal = request.POST.get('unidad_vecinal')
        identificacion_inmueble.region = request.POST.get('region')
        identificacion_inmueble.comuna = request.POST.get('comuna')
        identificacion_inmueble.calle = request.POST.get('calle')
        identificacion_inmueble.numero = request.POST.get('numero')
        identificacion_inmueble.plan_cerro_poblacion = request.POST.get('plan_cerro_poblacion')
        identificacion_inmueble.denominacion_inmueble = request.POST.get('denominacion_inmueble')
        identificacion_inmueble.autor = request.POST.get('autor')
        identificacion_inmueble.save()

        # Sección 2
        if request.FILES.get('imagen_plano'):
            plano_ubicacion.imagen_plano = request.FILES.get('imagen_plano')
        plano_ubicacion.latitud = request.POST.get('latitud')
        plano_ubicacion.longitud = request.POST.get('longitud')
        plano_ubicacion.save()

        # Sección 3
        if request.FILES.get('imagen_fotografia'):
            fotografia_general.imagen_fotografia = request.FILES.get('imagen_fotografia')
            fotografia_general.save()

        # Sección 4
        if request.FILES.get('registro_fotografico_1'):
            fotografia_contexto.registro_fotografico_1 = request.FILES.get('registro_fotografico_1')
        
        if request.FILES.get('registro_fotografico_2'):
            fotografia_contexto.registro_fotografico_2 = request.FILES.get('registro_fotografico_2')

        if request.POST.get('fecha_registro_fotografico'):
            fotografia_contexto.fecha_registro_fotografico = request.POST.get('fecha_registro_fotografico')
        

        fotografia_contexto.save()

        # Sección 5
        resena_patrimonial.valor_urbano = request.POST.get('valor_urbano')
        resena_patrimonial.valor_arquitecnico = request.POST.get('valor_arquitecnico')
        resena_patrimonial.valor_historico = request.POST.get('valor_historico')
        resena_patrimonial.valor_economico_social = request.POST.get('valor_economico_social')
        resena_patrimonial.save()

        # Sección 6
        valoracion_atributos.valor_urbano_a = request.POST.get('valor_urbano_a')
        valoracion_atributos.valor_urbano_b = request.POST.get('valor_urbano_b')
        valoracion_atributos.valor_urbano_c = request.POST.get('valor_urbano_c')
        valoracion_atributos.valor_arquitecnico_a = request.POST.get('valor_arquitecnico_a')
        valoracion_atributos.valor_arquitecnico_b = request.POST.get('valor_arquitecnico_b')
        valoracion_atributos.valor_arquitecnico_c = request.POST.get('valor_arquitecnico_c')
        valoracion_atributos.valor_historico_a = request.POST.get('valor_historico_a')
        valoracion_atributos.valor_historico_b = request.POST.get('valor_historico_b')
        valoracion_atributos.valor_economico_social_a = request.POST.get('valor_economico_social_a')
        valoracion_atributos.valor_economico_social_b = request.POST.get('valor_economico_social_b')
        valoracion_atributos.valor_economico_social_c = request.POST.get('valor_economico_social_c')
        valoracion_atributos.zona_de_conservacion = request.POST.get('zona_de_conservacion')
        valoracion_atributos.identificacion_zch = request.POST.get('identificacion_zch')
        valoracion_atributos.save()

        # Sección 7
        informacion_tecnica.piso_original_subterraneo = request.POST.get('piso_original_subterraneo')
        informacion_tecnica.piso_original_primer_piso = request.POST.get('piso_original_primer_piso')
        informacion_tecnica.piso_original_pisos_superiores = request.POST.get('piso_original_pisos_superiores')
        informacion_tecnica.piso_actual_subterraneo = request.POST.get('piso_actual_subterraneo')
        informacion_tecnica.piso_actual_primer_piso = request.POST.get('piso_actual_primer_piso')
        informacion_tecnica.piso_actual_pisos_superiores = request.POST.get('piso_actual_pisos_superiores')
        informacion_tecnica.anio_construccion = request.POST.get('anio_construccion')
        informacion_tecnica.tipo_propiedad = request.POST.get('tipo_propiedad')
        informacion_tecnica.tipo_usuario = request.POST.get('tipo_usuario')
        informacion_tecnica.regimen_propiedad = request.POST.get('regimen_propiedad')
        informacion_tecnica.afectacion_actual = request.POST.get('afectacion_actual')
        informacion_tecnica.observaciones = request.POST.get('informacion_tecnica_observaciones')
        informacion_tecnica.save()

        # Sección 8

        # Tipologia
        if not request.POST.get('manzana'):
            tipologia.manzana = False
        elif request.POST.get('manzana') and request.POST.get('manzana') == '1':
            tipologia.manzana = True

        if not request.POST.get('esquina'):
            tipologia.esquina = False
        elif request.POST.get('esquina') and request.POST.get('esquina') == '1':
            tipologia.esquina = True

        if not request.POST.get('entre_medianeros'):
            tipologia.entre_medianeros = False
        elif request.POST.get('entre_medianeros') and request.POST.get('entre_medianeros') == '1':
            tipologia.entre_medianeros = True

        if not request.POST.get('cabezal'):
            tipologia.cabezal = False
        elif request.POST.get('cabezal') and request.POST.get('cabezal') == '1':
            tipologia.cabezal = True

        if not request.POST.get('crucero'):
            tipologia.crucero = False
        elif request.POST.get('crucero') and request.POST.get('crucero') == '1':
            tipologia.crucero = True

        if not request.POST.get('doble_frente'):
            tipologia.doble_frente = False
        elif request.POST.get('doble_frente') and request.POST.get('doble_frente') == '1':
            tipologia.doble_frente = True

        if not request.POST.get('antejardines'):
            tipologia.antejardines = False
        elif request.POST.get('antejardines') and request.POST.get('antejardines') == '1':
            tipologia.antejardines = True

        tipologia.save()

        # Tipo Cubierta
        if not request.POST.get('horizontal'):
            tipo_cubierta.horizontal = False
        elif request.POST.get('horizontal') and request.POST.get('horizontal') == '1':
            tipo_cubierta.horizontal = True

        if not request.POST.get('inclinada'):
            tipo_cubierta.inclinada = False
        elif request.POST.get('inclinada') and request.POST.get('inclinada') == '1':
            tipo_cubierta.inclinada = True

        if not request.POST.get('curva'):
            tipo_cubierta.curva = False
        elif request.POST.get('curva') and request.POST.get('curva') == '1':
            tipo_cubierta.curva = True

        if not request.POST.get('tipo_cubierta_otro'):
            tipo_cubierta.otro = False
        elif request.POST.get('tipo_cubierta_otro') and request.POST.get('tipo_cubierta_otro') == '1':
            tipo_cubierta.otro = True

        tipo_cubierta.otro_texto = request.POST.get('tipo_cubierta_otro_texto')
        tipo_cubierta.save()

        # Elementos de valor Significativo

        if not request.POST.get('cornisamientos'):
            elementos_valor_significativo.cornisamientos = False
        elif request.POST.get('cornisamientos') and request.POST.get('cornisamientos') == '1':
            elementos_valor_significativo.cornisamientos = True

        if not request.POST.get('zocalos'):
            elementos_valor_significativo.zocalos = False
        elif request.POST.get('zocalos') and request.POST.get('zocalos') == '1':
            elementos_valor_significativo.zocalos = True

        if not request.POST.get('molduras_relevantes_en_yeso'):
            elementos_valor_significativo.molduras_relevantes_en_yeso = False
        elif request.POST.get('molduras_relevantes_en_yeso') and request.POST.get('molduras_relevantes_en_yeso') == '1':
            elementos_valor_significativo.molduras_relevantes_en_yeso = True

        if not request.POST.get('ornamentacion_en_madera'):
            elementos_valor_significativo.ornamentacion_en_madera = False
        elif request.POST.get('ornamentacion_en_madera') and request.POST.get('ornamentacion_en_madera') == '1':
            elementos_valor_significativo.ornamentacion_en_madera = True

        if not request.POST.get('remate_en_techumbre'):
            elementos_valor_significativo.remate_en_techumbre = False
        elif request.POST.get('remate_en_techumbre') and request.POST.get('remate_en_techumbre') == '1':
            elementos_valor_significativo.remate_en_techumbre = True

        if not request.POST.get('elementos_valor_significativo_otro'):
            elementos_valor_significativo.otro = False
        elif request.POST.get('elementos_valor_significativo_otro') and request.POST.get('elementos_valor_significativo_otro') == '1':
            elementos_valor_significativo.otro = True

        elementos_valor_significativo.otro_texto = request.POST.get('elementos_valor_significativo_otro_texto')
        elementos_valor_significativo.save()
            

        # Expresión de Fachada
        if not request.POST.get('lenguaje_de_vanos_comun'):
            expresion_fachada.lenguaje_de_vanos_comun = False
        elif request.POST.get('lenguaje_de_vanos_comun') and request.POST.get('lenguaje_de_vanos_comun') == '1':
            expresion_fachada.lenguaje_de_vanos_comun = True

        if not request.POST.get('simetria'):
            expresion_fachada.simetria = False
        elif request.POST.get('simetria') and request.POST.get('simetria') == '1':
            expresion_fachada.simetria = True

        if not request.POST.get('modulacion_en_serie'):
            expresion_fachada.modulacion_en_serie = False
        elif request.POST.get('modulacion_en_serie') and request.POST.get('modulacion_en_serie') == '1':
            expresion_fachada.modulacion_en_serie = True

        if not request.POST.get('torreon_en_esquina'):
            expresion_fachada.torreon_en_esquina = False
        elif request.POST.get('torreon_en_esquina') and request.POST.get('torreon_en_esquina') == '1':
            expresion_fachada.torreon_en_esquina = True

        if not request.POST.get('expresion_fachada_otro'):
            expresion_fachada.otro = False
        elif request.POST.get('expresion_fachada_otro') and request.POST.get('expresion_fachada_otro') == '1':
            expresion_fachada.otro = True

        expresion_fachada.otro_texto = request.POST.get('expresion_fachada_otro_texto')
        expresion_fachada.save()


        # Continuidad de Edificación
        if not request.POST.get('fachada'):
            continuidad_edificacion.otro = False
        elif request.POST.get('fachada') and request.POST.get('fachada') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_remate_superior'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_remate_superior') and request.POST.get('linea_de_remate_superior') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_zocalo_escalonado'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_zocalo_escalonado') and request.POST.get('linea_de_zocalo_escalonado') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_zocalo_continuo'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_zocalo_continuo') and request.POST.get('linea_de_zocalo_continuo') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('realce_horizontal_prodominante'):
            continuidad_edificacion.otro = False
        elif request.POST.get('realce_horizontal_prodominante') and request.POST.get('realce_horizontal_prodominante') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('zocalo_de_mamposteria'):
            continuidad_edificacion.otro = False
        elif request.POST.get('zocalo_de_mamposteria') and request.POST.get('zocalo_de_mamposteria') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('continuidad_edificacion_otro'):
            continuidad_edificacion.otro = False
        elif request.POST.get('continuidad_edificacion_otro') and request.POST.get('continuidad_edificacion_otro') == '1':
            continuidad_edificacion.otro = True

        continuidad_edificacion.otro_texto = request.POST.get('continuidad_edificacion_otro_texto')
        continuidad_edificacion.save()
        
        # Caracteristicas Morfológicas
        caracteristicas_morfologicas.sistema_agrupamiento = request.POST.get('sistema_agrupamiento')
        caracteristicas_morfologicas.volumetria = request.POST.get('volumetria')
        caracteristicas_morfologicas.observaciones = request.POST.get('caracteristicas_morfologicas_observaciones')

        if request.FILES.get('fotografia_valor_significativo'):
            caracteristicas_morfologicas.fotografia_valor_significativo = request.FILES.get('fotografia_valor_significativo')

        if request.FILES.get('fotografia_expresion_fachada'):
            caracteristicas_morfologicas.fotografia_expresion_fachada = request.FILES.get('fotografia_expresion_fachada')

        if request.FILES.get('fotografia_detalles_constructivos'):
            caracteristicas_morfologicas.fotografia_detalles_constructivos = request.FILES.get('fotografia_detalles_constructivos')

        caracteristicas_morfologicas.terreno = request.POST.get('terreno')
        caracteristicas_morfologicas.edificada = request.POST.get('edificada')
        caracteristicas_morfologicas.protegida = request.POST.get('protegida')
        caracteristicas_morfologicas.altura_en_pisos = request.POST.get('altura_en_pisos')
        caracteristicas_morfologicas.altura_en_metros = request.POST.get('altura_en_metros')
        caracteristicas_morfologicas.antejardin_frente_1 = request.POST.get('antejardin_frente_1')
        caracteristicas_morfologicas.antejardin_frente_2 = request.POST.get('antejardin_frente_2')

        caracteristicas_morfologicas.materialidad_estructura = request.POST.get('materialidad_estructura')
        caracteristicas_morfologicas.materialidad_cubierta = request.POST.get('materialidad_cubierta')

        
        if request.POST.get('materialidad_revestimientos') == "OTRO":
            caracteristicas_morfologicas.materialidad_revestimientos =  request.POST.get('materialidad_revestimientos_text')
        else:
            caracteristicas_morfologicas.materialidad_revestimientos =  request.POST.get('materialidad_revestimientos')

        caracteristicas_morfologicas.descripcion_del_inmubebles = request.POST.get('descripcion_del_inmubebles')

        caracteristicas_morfologicas.save()

        # Sección 9
        estado_de_conservacion.inmueble = request.POST.get('inmueble')
        estado_de_conservacion.entorno = request.POST.get('entorno')
        estado_de_conservacion.save()

        # Sección 10
        grado_de_alteracion.fachada = request.POST.get('grado_de_alteracion_fachada')
        grado_de_alteracion.cubierta = request.POST.get('grado_de_alteracion_cubierta')
        grado_de_alteracion.save()

        # Sección 11
        if not request.POST.get('vivienda'):
            aptitud_de_rehabilitacion.vivienda = False
        elif request.POST.get('vivienda') and request.POST.get('vivienda') == '1':
            aptitud_de_rehabilitacion.otro = True

        if not request.POST.get('equipamiento'):
            aptitud_de_rehabilitacion.equipamiento = False
        elif request.POST.get('equipamiento') and request.POST.get('equipamiento') == '1':
            aptitud_de_rehabilitacion.equipamiento = True

        if not request.POST.get('comercio'):
            aptitud_de_rehabilitacion.comercio = False
        elif request.POST.get('comercio') and request.POST.get('comercio') == '1':
            aptitud_de_rehabilitacion.comercio = True

        if not request.POST.get('aptitud_de_rehabilitacion_otro'):
            aptitud_de_rehabilitacion.otro = False
        elif request.POST.get('aptitud_de_rehabilitacion_otro') and request.POST.get('aptitud_de_rehabilitacion_otro') == '1':
            aptitud_de_rehabilitacion.otro = True

        aptitud_de_rehabilitacion.otro_texto = request.POST.get('aptitud_de_rehabilitacion_otro_texto')
        aptitud_de_rehabilitacion.save()

        # Sección 12
        if not request.POST.get('imagen_urbana_relevante_por_ubicacion'):
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_ubicacion = False
        elif request.POST.get('imagen_urbana_relevante_por_ubicacion') and request.POST.get('imagen_urbana_relevante_por_ubicacion') == '1':
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_ubicacion = True

        if not request.POST.get('imagen_urbana_relevante_por_singularidad'):
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_singularidad = False
        elif request.POST.get('imagen_urbana_relevante_por_singularidad') and request.POST.get('imagen_urbana_relevante_por_singularidad') == '1':
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_singularidad = True

        if not request.POST.get('forma_parte_de_un_conjunto'):
            relacion_del_inmueble_con_el_terreno.forma_parte_de_un_conjunto = False
        elif request.POST.get('forma_parte_de_un_conjunto') and request.POST.get('forma_parte_de_un_conjunto') == '1':
            relacion_del_inmueble_con_el_terreno.forma_parte_de_un_conjunto = True
        
        relacion_del_inmueble_con_el_terreno.espacio_publico = request.POST.get('espacio_publico')
        # relacion_del_inmueble_con_el_terreno.monumentos_historicos = request.POST.get('monumentos_historicos')
        # relacion_del_inmueble_con_el_terreno.inmuebles_conservacion_historica = request.POST.get('inmuebles_conservacion_historica')

        # 12.5 Monumentos históricos
        if not request.POST.get('mon_his_predio_contiguo'):
            relacion_del_inmueble_con_el_terreno.mon_his_predio_contiguo = False
        elif request.POST.get('mon_his_predio_contiguo') and request.POST.get('mon_his_predio_contiguo') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_predio_contiguo = True

        if not request.POST.get('mon_his_manzana'):
            relacion_del_inmueble_con_el_terreno.mon_his_manzana = False
        elif request.POST.get('mon_his_manzana') and request.POST.get('mon_his_manzana') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_manzana = True

        if not request.POST.get('mon_his_manzana_enfrente'):
            relacion_del_inmueble_con_el_terreno.mon_his_manzana_enfrente = False
        elif request.POST.get('mon_his_manzana_enfrente') and request.POST.get('mon_his_manzana_enfrente') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_manzana_enfrente = True

        if not request.POST.get('mon_his_relacion_visual'):
            relacion_del_inmueble_con_el_terreno.mon_his_relacion_visual = False
        elif request.POST.get('mon_his_relacion_visual') and request.POST.get('mon_his_relacion_visual') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_relacion_visual = True

        # 12.5 Inmuebles de conservación histórica
        if not request.POST.get('inm_con_his_predio_contiguo'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_predio_contiguo = False
        elif request.POST.get('inm_con_his_predio_contiguo') and request.POST.get('inm_con_his_predio_contiguo') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_predio_contiguo = True

        if not request.POST.get('inm_con_his_manzana'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana = False
        elif request.POST.get('inm_con_his_manzana') and request.POST.get('inm_con_his_manzana') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana = True
        
        if not request.POST.get('inm_con_his_manzana_enfrente'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana_enfrente = False
        elif request.POST.get('inm_con_his_manzana_enfrente') and request.POST.get('inm_con_his_manzana_enfrente') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana_enfrente = True

        if not request.POST.get('inm_con_his_relacion_visual'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_relacion_visual = False
        elif request.POST.get('inm_con_his_relacion_visual') and request.POST.get('inm_con_his_relacion_visual') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_relacion_visual = True

        relacion_del_inmueble_con_el_terreno.observaciones = request.POST.get('espacio_publico_observaciones')
        relacion_del_inmueble_con_el_terreno.Otros_elementos_patrimonial = request.POST.get('Otros_elementos_patrimonial')
        relacion_del_inmueble_con_el_terreno.save()

        # Sección 13
        # categoria_de_acuerdo_a_su_uso.observaciones = request.POST.get('categoria_de_acuerdo_a_su_uso_observaciones')
        # categoria_de_acuerdo_a_su_uso.save()

        # Sección 14
        conclusiones.conclusiones = request.POST.get('conclusiones')
        conclusiones.save()

        # Sección 15
        fuentes_referenciales_y_bibliograficas.fuentes_referenciales_y_bibliograficas = request.POST.get('fuentes_referenciales_y_bibliograficas')
        fuentes_referenciales_y_bibliograficas.save()




    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
        'fotografia_general': fotografia_general,
        'fotografia_contexto': fotografia_contexto,
        'resena_patrimonial': resena_patrimonial,
        'valoracion_atributos': valoracion_atributos,
        'informacion_tecnica': informacion_tecnica,
        'caracteristicas_morfologicas': caracteristicas_morfologicas,
        'estado_de_conservacion': estado_de_conservacion,
        'grado_de_alteracion': grado_de_alteracion,
        'aptitud_de_rehabilitacion': aptitud_de_rehabilitacion,
        'relacion_del_inmueble_con_el_terreno': relacion_del_inmueble_con_el_terreno,
        'categoria_de_acuerdo_a_su_uso': categoria_de_acuerdo_a_su_uso,
        'conclusiones': conclusiones,
        'fuentes_referenciales_y_bibliograficas': fuentes_referenciales_y_bibliograficas,

        'tipologia': tipologia,
        'tipo_cubierta': tipo_cubierta,
        'elementos_valor_significativo': elementos_valor_significativo,
        'expresion_fachada': expresion_fachada,
        'continuidad_edificacion': continuidad_edificacion,

        'OPTIONS': OPTIONS,

        'total_valor_urbano': total_valor_urbano,
        'total_valor_arquitecnico': total_valor_arquitecnico,
        'total_valor_historico': total_valor_historico,
        'total_valor_economico_social': total_valor_economico_social,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'ficha/crear_ficha.html', data)

@login_required(login_url='/login/')
def editar_ficha(request, id = 0):
    
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    plano_ubicacion = PlanoUbicacion.objects.get(id_plano = id)
    fotografia_general = FotografiaGeneral.objects.get(id_plano = id)
    fotografia_contexto = FotografiaContexto.objects.get(id_plano = id)
    resena_patrimonial = ResenaPatrimonial.objects.get(id_plano = id)
    valoracion_atributos = ValoracionAtributos.objects.get(id_plano = id)
    informacion_tecnica = InformacionTecnica.objects.get(id_plano = id)
    caracteristicas_morfologicas = CaracteristicasMorfologicas.objects.get(id_plano = id)
    estado_de_conservacion = EstadoDeConservacion.objects.get(id_plano = id)
    grado_de_alteracion = GradoDeAlteracion.objects.get(id_plano = id)
    aptitud_de_rehabilitacion = AptitudDeRehabilitacion.objects.get(id_plano = id)
    relacion_del_inmueble_con_el_terreno = RelacionDelInmuebleConElTerreno.objects.get(id_plano = id)
    categoria_de_acuerdo_a_su_uso = CategoriaDeAcuerdoASuUso.objects.get(id_plano = id)
    conclusiones = Conclusiones.objects.get(id_plano = id)
    fuentes_referenciales_y_bibliograficas = FuentesReferencialesYBibliograficas.objects.get(id_plano = id)

    tipologia = Tipologias.objects.get(id_plano_id = id)
    tipo_cubierta = TipoCubierta.objects.get(id_plano_id = id)
    elementos_valor_significativo = ElementosValorSignificativo.objects.get(id_plano_id = id)
    expresion_fachada = ExpresionDeFachada.objects.get(id_plano_id = id)
    continuidad_edificacion = ContinuidadDeEdificacion.objects.get(id_plano_id = id)


    OPTIONS = {
        'PLAN_CERRO_POBLACION': PLAN_CERRO_POBLACION,
        'REGION_CHOICES': REGION_CHOICES,
        'COMUNA_CHOICES': COMUNA_CHOICES,
        'PERIODOS_CONSTRUCCION': PERIODOS_CONSTRUCCION,
        'TIPO_DESTINO_INMUEBLE': TIPO_DESTINO_INMUEBLE,
        'TIPO_PROPIEDAD': TIPO_PROPIEDAD,
        'TIPO_USUARIO': TIPO_USUARIO,
        'REGIMEN_PROPIEDAD': REGIMEN_PROPIEDAD,
        'AFECTACION_ACTUAL': AFECTACION_ACTUAL,
        'SISTEMA_AGRUPAMIENTO': SISTEMA_AGRUPAMIENTO,
        'VOLUMETRIA': VOLUMETRIA,
        'MATERIALIDAD_ESTRUCTURA': MATERIALIDAD_ESTRUCTURA,
        'MATERIALIDAD_CUBIERTA': MATERIALIDAD_CUBIERTA,
        'SISTEMA_AGRUPAMIENTO': SISTEMA_AGRUPAMIENTO,
        'VOLUMETRIA': VOLUMETRIA,
        'MATERIALIDAD_ESTRUCTURA': MATERIALIDAD_ESTRUCTURA,
        'MATERIALIDAD_CUBIERTA': MATERIALIDAD_CUBIERTA,
        'ESTADO_CONSERVACION': ESTADO_CONSERVACION,
        'GRADO_ALTERACION': GRADO_ALTERACION,
        'ESPACIO_PUBLICO': ESPACIO_PUBLICO,
        'INMUEBLES_PATRIMONIALES': INMUEBLES_PATRIMONIALES,
        'PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL': PRESENCIA_ELEMENTOS_VALOR_PATRIMONIAL,
        'MATERIALIDAD_REVESTIMIENTO': MATERIALIDAD_REVESTIMIENTO,
    }

    # Sección 6
    total_valor_urbano = valoracion_atributos.valor_urbano_a + valoracion_atributos.valor_urbano_b + valoracion_atributos.valor_urbano_c
    total_valor_arquitecnico = valoracion_atributos.valor_arquitecnico_a + valoracion_atributos.valor_arquitecnico_b + valoracion_atributos.valor_arquitecnico_c
    total_valor_historico = valoracion_atributos.valor_historico_a + valoracion_atributos.valor_historico_b
    total_valor_economico_social = valoracion_atributos.valor_economico_social_a + valoracion_atributos.valor_economico_social_b + valoracion_atributos.valor_economico_social_c
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico_social

    if request.method == 'POST':
        # Sección 1
        identificacion_inmueble.rol = request.POST.get('rol')
        identificacion_inmueble.unidad_vecinal = request.POST.get('unidad_vecinal')
        identificacion_inmueble.region = request.POST.get('region')
        identificacion_inmueble.comuna = request.POST.get('comuna')
        identificacion_inmueble.calle = request.POST.get('calle')
        identificacion_inmueble.numero = request.POST.get('numero')
        identificacion_inmueble.plan_cerro_poblacion = request.POST.get('plan_cerro_poblacion')
        identificacion_inmueble.denominacion_inmueble = request.POST.get('denominacion_inmueble')
        identificacion_inmueble.autor = request.POST.get('autor')
        identificacion_inmueble.save()

        # Sección 2
        if request.FILES.get('imagen_plano'):
            plano_ubicacion.imagen_plano = request.FILES.get('imagen_plano')
        plano_ubicacion.latitud = request.POST.get('latitud')
        plano_ubicacion.longitud = request.POST.get('longitud')
        plano_ubicacion.save()

        # Sección 3
        if request.FILES.get('imagen_fotografia'):
            fotografia_general.imagen_fotografia = request.FILES.get('imagen_fotografia')
            fotografia_general.save()

        # Sección 4
        if request.FILES.get('registro_fotografico_1'):
            fotografia_contexto.registro_fotografico_1 = request.FILES.get('registro_fotografico_1')
        
        if request.FILES.get('registro_fotografico_2'):
            fotografia_contexto.registro_fotografico_2 = request.FILES.get('registro_fotografico_2')

        if request.POST.get('fecha_registro_fotografico'):
            fotografia_contexto.fecha_registro_fotografico = request.POST.get('fecha_registro_fotografico')
        

        fotografia_contexto.save()

        # Sección 5
        resena_patrimonial.valor_urbano = request.POST.get('valor_urbano')
        resena_patrimonial.valor_arquitecnico = request.POST.get('valor_arquitecnico')
        resena_patrimonial.valor_historico = request.POST.get('valor_historico')
        resena_patrimonial.valor_economico_social = request.POST.get('valor_economico_social')
        resena_patrimonial.save()

        # Sección 6
        valoracion_atributos.valor_urbano_a = request.POST.get('valor_urbano_a')
        valoracion_atributos.valor_urbano_b = request.POST.get('valor_urbano_b')
        valoracion_atributos.valor_urbano_c = request.POST.get('valor_urbano_c')
        valoracion_atributos.valor_arquitecnico_a = request.POST.get('valor_arquitecnico_a')
        valoracion_atributos.valor_arquitecnico_b = request.POST.get('valor_arquitecnico_b')
        valoracion_atributos.valor_arquitecnico_c = request.POST.get('valor_arquitecnico_c')
        valoracion_atributos.valor_historico_a = request.POST.get('valor_historico_a')
        valoracion_atributos.valor_historico_b = request.POST.get('valor_historico_b')
        valoracion_atributos.valor_economico_social_a = request.POST.get('valor_economico_social_a')
        valoracion_atributos.valor_economico_social_b = request.POST.get('valor_economico_social_b')
        valoracion_atributos.valor_economico_social_c = request.POST.get('valor_economico_social_c')
        valoracion_atributos.zona_de_conservacion = request.POST.get('zona_de_conservacion')
        valoracion_atributos.identificacion_zch = request.POST.get('identificacion_zch')
        valoracion_atributos.save()

        # Sección 7
        informacion_tecnica.piso_original_subterraneo = request.POST.get('piso_original_subterraneo')
        informacion_tecnica.piso_original_primer_piso = request.POST.get('piso_original_primer_piso')
        informacion_tecnica.piso_original_pisos_superiores = request.POST.get('piso_original_pisos_superiores')
        informacion_tecnica.piso_actual_subterraneo = request.POST.get('piso_actual_subterraneo')
        informacion_tecnica.piso_actual_primer_piso = request.POST.get('piso_actual_primer_piso')
        informacion_tecnica.piso_actual_pisos_superiores = request.POST.get('piso_actual_pisos_superiores')
        informacion_tecnica.anio_construccion = request.POST.get('anio_construccion')
        informacion_tecnica.tipo_propiedad = request.POST.get('tipo_propiedad')
        informacion_tecnica.tipo_usuario = request.POST.get('tipo_usuario')
        informacion_tecnica.regimen_propiedad = request.POST.get('regimen_propiedad')
        informacion_tecnica.afectacion_actual = request.POST.get('afectacion_actual')
        informacion_tecnica.observaciones = request.POST.get('informacion_tecnica_observaciones')
        informacion_tecnica.save()

        # Sección 8

        # Tipologia
        if not request.POST.get('manzana'):
            tipologia.manzana = False
        elif request.POST.get('manzana') and request.POST.get('manzana') == '1':
            tipologia.manzana = True

        if not request.POST.get('esquina'):
            tipologia.esquina = False
        elif request.POST.get('esquina') and request.POST.get('esquina') == '1':
            tipologia.esquina = True

        if not request.POST.get('entre_medianeros'):
            tipologia.entre_medianeros = False
        elif request.POST.get('entre_medianeros') and request.POST.get('entre_medianeros') == '1':
            tipologia.entre_medianeros = True

        if not request.POST.get('cabezal'):
            tipologia.cabezal = False
        elif request.POST.get('cabezal') and request.POST.get('cabezal') == '1':
            tipologia.cabezal = True

        if not request.POST.get('crucero'):
            tipologia.crucero = False
        elif request.POST.get('crucero') and request.POST.get('crucero') == '1':
            tipologia.crucero = True

        if not request.POST.get('doble_frente'):
            tipologia.doble_frente = False
        elif request.POST.get('doble_frente') and request.POST.get('doble_frente') == '1':
            tipologia.doble_frente = True

        if not request.POST.get('antejardines'):
            tipologia.antejardines = False
        elif request.POST.get('antejardines') and request.POST.get('antejardines') == '1':
            tipologia.antejardines = True

        tipologia.save()

        # Tipo Cubierta
        if not request.POST.get('horizontal'):
            tipo_cubierta.horizontal = False
        elif request.POST.get('horizontal') and request.POST.get('horizontal') == '1':
            tipo_cubierta.horizontal = True

        if not request.POST.get('inclinada'):
            tipo_cubierta.inclinada = False
        elif request.POST.get('inclinada') and request.POST.get('inclinada') == '1':
            tipo_cubierta.inclinada = True

        if not request.POST.get('curva'):
            tipo_cubierta.curva = False
        elif request.POST.get('curva') and request.POST.get('curva') == '1':
            tipo_cubierta.curva = True

        if not request.POST.get('tipo_cubierta_otro'):
            tipo_cubierta.otro = False
        elif request.POST.get('tipo_cubierta_otro') and request.POST.get('tipo_cubierta_otro') == '1':
            tipo_cubierta.otro = True

        tipo_cubierta.otro_texto = request.POST.get('tipo_cubierta_otro_texto')
        tipo_cubierta.save()

        # Elementos de valor Significativo

        if not request.POST.get('cornisamientos'):
            elementos_valor_significativo.cornisamientos = False
        elif request.POST.get('cornisamientos') and request.POST.get('cornisamientos') == '1':
            elementos_valor_significativo.cornisamientos = True

        if not request.POST.get('zocalos'):
            elementos_valor_significativo.zocalos = False
        elif request.POST.get('zocalos') and request.POST.get('zocalos') == '1':
            elementos_valor_significativo.zocalos = True

        if not request.POST.get('molduras_relevantes_en_yeso'):
            elementos_valor_significativo.molduras_relevantes_en_yeso = False
        elif request.POST.get('molduras_relevantes_en_yeso') and request.POST.get('molduras_relevantes_en_yeso') == '1':
            elementos_valor_significativo.molduras_relevantes_en_yeso = True

        if not request.POST.get('ornamentacion_en_madera'):
            elementos_valor_significativo.ornamentacion_en_madera = False
        elif request.POST.get('ornamentacion_en_madera') and request.POST.get('ornamentacion_en_madera') == '1':
            elementos_valor_significativo.ornamentacion_en_madera = True

        if not request.POST.get('remate_en_techumbre'):
            elementos_valor_significativo.remate_en_techumbre = False
        elif request.POST.get('remate_en_techumbre') and request.POST.get('remate_en_techumbre') == '1':
            elementos_valor_significativo.remate_en_techumbre = True

        if not request.POST.get('elementos_valor_significativo_otro'):
            elementos_valor_significativo.otro = False
        elif request.POST.get('elementos_valor_significativo_otro') and request.POST.get('elementos_valor_significativo_otro') == '1':
            elementos_valor_significativo.otro = True

        elementos_valor_significativo.otro_texto = request.POST.get('elementos_valor_significativo_otro_texto')
        elementos_valor_significativo.save()
            

        # Expresión de Fachada
        if not request.POST.get('lenguaje_de_vanos_comun'):
            expresion_fachada.lenguaje_de_vanos_comun = False
        elif request.POST.get('lenguaje_de_vanos_comun') and request.POST.get('lenguaje_de_vanos_comun') == '1':
            expresion_fachada.lenguaje_de_vanos_comun = True

        if not request.POST.get('simetria'):
            expresion_fachada.simetria = False
        elif request.POST.get('simetria') and request.POST.get('simetria') == '1':
            expresion_fachada.simetria = True

        if not request.POST.get('modulacion_en_serie'):
            expresion_fachada.modulacion_en_serie = False
        elif request.POST.get('modulacion_en_serie') and request.POST.get('modulacion_en_serie') == '1':
            expresion_fachada.modulacion_en_serie = True

        if not request.POST.get('torreon_en_esquina'):
            expresion_fachada.torreon_en_esquina = False
        elif request.POST.get('torreon_en_esquina') and request.POST.get('torreon_en_esquina') == '1':
            expresion_fachada.torreon_en_esquina = True

        if not request.POST.get('expresion_fachada_otro'):
            expresion_fachada.otro = False
        elif request.POST.get('expresion_fachada_otro') and request.POST.get('expresion_fachada_otro') == '1':
            expresion_fachada.otro = True

        expresion_fachada.otro_texto = request.POST.get('expresion_fachada_otro_texto')
        expresion_fachada.save()


        # Continuidad de Edificación
        if not request.POST.get('fachada'):
            continuidad_edificacion.otro = False
        elif request.POST.get('fachada') and request.POST.get('fachada') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_remate_superior'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_remate_superior') and request.POST.get('linea_de_remate_superior') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_zocalo_escalonado'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_zocalo_escalonado') and request.POST.get('linea_de_zocalo_escalonado') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('linea_de_zocalo_continuo'):
            continuidad_edificacion.otro = False
        elif request.POST.get('linea_de_zocalo_continuo') and request.POST.get('linea_de_zocalo_continuo') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('realce_horizontal_prodominante'):
            continuidad_edificacion.otro = False
        elif request.POST.get('realce_horizontal_prodominante') and request.POST.get('realce_horizontal_prodominante') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('zocalo_de_mamposteria'):
            continuidad_edificacion.otro = False
        elif request.POST.get('zocalo_de_mamposteria') and request.POST.get('zocalo_de_mamposteria') == '1':
            continuidad_edificacion.otro = True

        if not request.POST.get('continuidad_edificacion_otro'):
            continuidad_edificacion.otro = False
        elif request.POST.get('continuidad_edificacion_otro') and request.POST.get('continuidad_edificacion_otro') == '1':
            continuidad_edificacion.otro = True

        continuidad_edificacion.otro_texto = request.POST.get('continuidad_edificacion_otro_texto')
        continuidad_edificacion.save()
        
        # Caracteristicas Morfológicas
        caracteristicas_morfologicas.sistema_agrupamiento = request.POST.get('sistema_agrupamiento')
        caracteristicas_morfologicas.volumetria = request.POST.get('volumetria')
        caracteristicas_morfologicas.observaciones = request.POST.get('caracteristicas_morfologicas_observaciones')

        if request.FILES.get('fotografia_valor_significativo'):
            caracteristicas_morfologicas.fotografia_valor_significativo = request.FILES.get('fotografia_valor_significativo')

        if request.FILES.get('fotografia_expresion_fachada'):
            caracteristicas_morfologicas.fotografia_expresion_fachada = request.FILES.get('fotografia_expresion_fachada')

        if request.FILES.get('fotografia_detalles_constructivos'):
            caracteristicas_morfologicas.fotografia_detalles_constructivos = request.FILES.get('fotografia_detalles_constructivos')

        caracteristicas_morfologicas.terreno = request.POST.get('terreno')
        caracteristicas_morfologicas.edificada = request.POST.get('edificada')
        caracteristicas_morfologicas.protegida = request.POST.get('protegida')
        caracteristicas_morfologicas.altura_en_pisos = request.POST.get('altura_en_pisos')
        caracteristicas_morfologicas.altura_en_metros = request.POST.get('altura_en_metros')
        caracteristicas_morfologicas.antejardin_frente_1 = request.POST.get('antejardin_frente_1')
        caracteristicas_morfologicas.antejardin_frente_2 = request.POST.get('antejardin_frente_2')

        caracteristicas_morfologicas.materialidad_estructura = request.POST.get('materialidad_estructura')
        caracteristicas_morfologicas.materialidad_cubierta = request.POST.get('materialidad_cubierta')

        
        if request.POST.get('materialidad_revestimientos') == "OTRO":
            caracteristicas_morfologicas.materialidad_revestimientos =  request.POST.get('materialidad_revestimientos_text')
        else:
            caracteristicas_morfologicas.materialidad_revestimientos =  request.POST.get('materialidad_revestimientos')

        caracteristicas_morfologicas.descripcion_del_inmubebles = request.POST.get('descripcion_del_inmubebles')

        caracteristicas_morfologicas.save()

        # Sección 9
        estado_de_conservacion.inmueble = request.POST.get('inmueble')
        estado_de_conservacion.entorno = request.POST.get('entorno')
        estado_de_conservacion.save()

        # Sección 10
        grado_de_alteracion.fachada = request.POST.get('grado_de_alteracion_fachada')
        grado_de_alteracion.cubierta = request.POST.get('grado_de_alteracion_cubierta')
        grado_de_alteracion.save()

        # Sección 11
        if not request.POST.get('vivienda'):
            aptitud_de_rehabilitacion.vivienda = False
        elif request.POST.get('vivienda') and request.POST.get('vivienda') == '1':
            aptitud_de_rehabilitacion.otro = True

        if not request.POST.get('equipamiento'):
            aptitud_de_rehabilitacion.equipamiento = False
        elif request.POST.get('equipamiento') and request.POST.get('equipamiento') == '1':
            aptitud_de_rehabilitacion.equipamiento = True

        if not request.POST.get('comercio'):
            aptitud_de_rehabilitacion.comercio = False
        elif request.POST.get('comercio') and request.POST.get('comercio') == '1':
            aptitud_de_rehabilitacion.comercio = True

        if not request.POST.get('aptitud_de_rehabilitacion_otro'):
            aptitud_de_rehabilitacion.otro = False
        elif request.POST.get('aptitud_de_rehabilitacion_otro') and request.POST.get('aptitud_de_rehabilitacion_otro') == '1':
            aptitud_de_rehabilitacion.otro = True

        aptitud_de_rehabilitacion.otro_texto = request.POST.get('aptitud_de_rehabilitacion_otro_texto')
        aptitud_de_rehabilitacion.save()

        # Sección 12
        if not request.POST.get('imagen_urbana_relevante_por_ubicacion'):
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_ubicacion = False
        elif request.POST.get('imagen_urbana_relevante_por_ubicacion') and request.POST.get('imagen_urbana_relevante_por_ubicacion') == '1':
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_ubicacion = True

        if not request.POST.get('imagen_urbana_relevante_por_singularidad'):
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_singularidad = False
        elif request.POST.get('imagen_urbana_relevante_por_singularidad') and request.POST.get('imagen_urbana_relevante_por_singularidad') == '1':
            relacion_del_inmueble_con_el_terreno.imagen_urbana_relevante_por_singularidad = True

        if not request.POST.get('forma_parte_de_un_conjunto'):
            relacion_del_inmueble_con_el_terreno.forma_parte_de_un_conjunto = False
        elif request.POST.get('forma_parte_de_un_conjunto') and request.POST.get('forma_parte_de_un_conjunto') == '1':
            relacion_del_inmueble_con_el_terreno.forma_parte_de_un_conjunto = True
        
        relacion_del_inmueble_con_el_terreno.espacio_publico = request.POST.get('espacio_publico')
        # relacion_del_inmueble_con_el_terreno.monumentos_historicos = request.POST.get('monumentos_historicos')
        # relacion_del_inmueble_con_el_terreno.inmuebles_conservacion_historica = request.POST.get('inmuebles_conservacion_historica')

        # 12.5 Monumentos históricos
        if not request.POST.get('mon_his_predio_contiguo'):
            relacion_del_inmueble_con_el_terreno.mon_his_predio_contiguo = False
        elif request.POST.get('mon_his_predio_contiguo') and request.POST.get('mon_his_predio_contiguo') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_predio_contiguo = True

        if not request.POST.get('mon_his_manzana'):
            relacion_del_inmueble_con_el_terreno.mon_his_manzana = False
        elif request.POST.get('mon_his_manzana') and request.POST.get('mon_his_manzana') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_manzana = True

        if not request.POST.get('mon_his_manzana_enfrente'):
            relacion_del_inmueble_con_el_terreno.mon_his_manzana_enfrente = False
        elif request.POST.get('mon_his_manzana_enfrente') and request.POST.get('mon_his_manzana_enfrente') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_manzana_enfrente = True

        if not request.POST.get('mon_his_relacion_visual'):
            relacion_del_inmueble_con_el_terreno.mon_his_relacion_visual = False
        elif request.POST.get('mon_his_relacion_visual') and request.POST.get('mon_his_relacion_visual') == '1':
            relacion_del_inmueble_con_el_terreno.mon_his_relacion_visual = True

        # 12.5 Inmuebles de conservación histórica
        if not request.POST.get('inm_con_his_predio_contiguo'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_predio_contiguo = False
        elif request.POST.get('inm_con_his_predio_contiguo') and request.POST.get('inm_con_his_predio_contiguo') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_predio_contiguo = True

        if not request.POST.get('inm_con_his_manzana'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana = False
        elif request.POST.get('inm_con_his_manzana') and request.POST.get('inm_con_his_manzana') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana = True
        
        if not request.POST.get('inm_con_his_manzana_enfrente'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana_enfrente = False
        elif request.POST.get('inm_con_his_manzana_enfrente') and request.POST.get('inm_con_his_manzana_enfrente') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_manzana_enfrente = True

        if not request.POST.get('inm_con_his_relacion_visual'):
            relacion_del_inmueble_con_el_terreno.inm_con_his_relacion_visual = False
        elif request.POST.get('inm_con_his_relacion_visual') and request.POST.get('inm_con_his_relacion_visual') == '1':
            relacion_del_inmueble_con_el_terreno.inm_con_his_relacion_visual = True

        relacion_del_inmueble_con_el_terreno.observaciones = request.POST.get('espacio_publico_observaciones')
        relacion_del_inmueble_con_el_terreno.Otros_elementos_patrimonial = request.POST.get('Otros_elementos_patrimonial')
        relacion_del_inmueble_con_el_terreno.save()

        # Sección 13
        # categoria_de_acuerdo_a_su_uso.observaciones = request.POST.get('categoria_de_acuerdo_a_su_uso_observaciones')
        # categoria_de_acuerdo_a_su_uso.save()

        # Sección 14
        conclusiones.conclusiones = request.POST.get('conclusiones')
        conclusiones.save()

        # Sección 15
        fuentes_referenciales_y_bibliograficas.fuentes_referenciales_y_bibliograficas = request.POST.get('fuentes_referenciales_y_bibliograficas')
        fuentes_referenciales_y_bibliograficas.save()




    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
        'fotografia_general': fotografia_general,
        'fotografia_contexto': fotografia_contexto,
        'resena_patrimonial': resena_patrimonial,
        'valoracion_atributos': valoracion_atributos,
        'informacion_tecnica': informacion_tecnica,
        'caracteristicas_morfologicas': caracteristicas_morfologicas,
        'estado_de_conservacion': estado_de_conservacion,
        'grado_de_alteracion': grado_de_alteracion,
        'aptitud_de_rehabilitacion': aptitud_de_rehabilitacion,
        'relacion_del_inmueble_con_el_terreno': relacion_del_inmueble_con_el_terreno,
        'categoria_de_acuerdo_a_su_uso': categoria_de_acuerdo_a_su_uso,
        'conclusiones': conclusiones,
        'fuentes_referenciales_y_bibliograficas': fuentes_referenciales_y_bibliograficas,

        'tipologia': tipologia,
        'tipo_cubierta': tipo_cubierta,
        'elementos_valor_significativo': elementos_valor_significativo,
        'expresion_fachada': expresion_fachada,
        'continuidad_edificacion': continuidad_edificacion,

        'OPTIONS': OPTIONS,

        'total_valor_urbano': total_valor_urbano,
        'total_valor_arquitecnico': total_valor_arquitecnico,
        'total_valor_historico': total_valor_historico,
        'total_valor_economico_social': total_valor_economico_social,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'ficha/editar_ficha.html', data)

@login_required(login_url='/login/')
def ver_fichas(request):
    identificacion_inmueble = IdentificacionInmueble.objects.all()

    data = {
        'fichas': identificacion_inmueble
    }
    return render(request, 'ficha/ver_fichas.html', data)

@login_required(login_url='/login/')
def ver_ficha(request, id):
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    plano_ubicacion = PlanoUbicacion.objects.get(id_plano = id)

    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
    }
    return render(request, 'ficha/ver_ficha.html', data)

def exportar_pdf(request, id):
    
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    plano_ubicacion = PlanoUbicacion.objects.get(id_plano = id)
    fotografia_general = FotografiaGeneral.objects.get(id_plano = id)
    fotografia_contexto = FotografiaContexto.objects.get(id_plano = id)
    resena_patrimonial = ResenaPatrimonial.objects.get(id_plano = id)
    valoracion_atributos = ValoracionAtributos.objects.get(id_plano = id)
    informacion_tecnica = InformacionTecnica.objects.get(id_plano = id)
    caracteristicas_morfologicas = CaracteristicasMorfologicas.objects.get(id_plano = id)
    estado_de_conservacion = EstadoDeConservacion.objects.get(id_plano = id)
    grado_de_alteracion = GradoDeAlteracion.objects.get(id_plano = id)
    aptitud_de_rehabilitacion = AptitudDeRehabilitacion.objects.get(id_plano = id)
    relacion_del_inmueble_con_el_terreno = RelacionDelInmuebleConElTerreno.objects.get(id_plano = id)
    categoria_de_acuerdo_a_su_uso = CategoriaDeAcuerdoASuUso.objects.get(id_plano = id)
    conclusiones = Conclusiones.objects.get(id_plano = id)
    fuentes_referenciales_y_bibliograficas = FuentesReferencialesYBibliograficas.objects.get(id_plano = id)

    tipologia = Tipologias.objects.get(id_plano_id = id)
    tipo_cubierta = TipoCubierta.objects.get(id_plano_id = id)
    elementos_valor_significativo = ElementosValorSignificativo.objects.get(id_plano_id = id)
    expresion_fachada = ExpresionDeFachada.objects.get(id_plano_id = id)
    continuidad_edificacion = ContinuidadDeEdificacion.objects.get(id_plano_id = id)

    # Sección 6
    total_valor_urbano = valoracion_atributos.valor_urbano_a + valoracion_atributos.valor_urbano_b + valoracion_atributos.valor_urbano_c
    total_valor_arquitecnico = valoracion_atributos.valor_arquitecnico_a + valoracion_atributos.valor_arquitecnico_b + valoracion_atributos.valor_arquitecnico_c
    total_valor_historico = valoracion_atributos.valor_historico_a + valoracion_atributos.valor_historico_b
    total_valor_economico_social = valoracion_atributos.valor_economico_social_a + valoracion_atributos.valor_economico_social_b + valoracion_atributos.valor_economico_social_c
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico_social

    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y_%H-%M-%S")
    current_user = request.user

    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
        'fotografia_general': fotografia_general,
        'fotografia_contexto': fotografia_contexto,
        'resena_patrimonial': resena_patrimonial,
        'valoracion_atributos': valoracion_atributos,
        'informacion_tecnica': informacion_tecnica,
        'caracteristicas_morfologicas': caracteristicas_morfologicas,
        'estado_de_conservacion': estado_de_conservacion,
        'grado_de_alteracion': grado_de_alteracion,
        'aptitud_de_rehabilitacion': aptitud_de_rehabilitacion,
        'relacion_del_inmueble_con_el_terreno': relacion_del_inmueble_con_el_terreno,
        'categoria_de_acuerdo_a_su_uso': categoria_de_acuerdo_a_su_uso,
        'conclusiones': conclusiones,
        'fuentes_referenciales_y_bibliograficas': fuentes_referenciales_y_bibliograficas,

        'tipologia': tipologia,
        'tipo_cubierta': tipo_cubierta,
        'elementos_valor_significativo': elementos_valor_significativo,
        'expresion_fachada': expresion_fachada,
        'continuidad_edificacion': continuidad_edificacion,

        'total_valor_urbano': total_valor_urbano,
        'total_valor_arquitecnico': total_valor_arquitecnico,
        'total_valor_historico': total_valor_historico,
        'total_valor_economico_social': total_valor_economico_social,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': request.build_absolute_uri('/')[:-1],

        'current_time': now,
        'current_user': current_user,
    }
    
    nombre_ficha = "ficha_" + str(identificacion_inmueble.id_plano) + "_" + current_time

    file_name, status = save_pdf_2(data, nombre_ficha)

    if not status:
        print("----------------")
        print("Error al generar PDF")
        print("----------------")
        return HttpResponse("Error al generar PDF")

    nombre_archivo = nombre_ficha + ".pdf"

    # return HttpResponse(file_name)
    return FileResponse(open(file_name, 'rb'), content_type='application/pdf', filename=nombre_archivo, as_attachment=True)

    
def test_pdf(request, id):
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    plano_ubicacion = PlanoUbicacion.objects.get(id_plano = id)
    fotografia_general = FotografiaGeneral.objects.get(id_plano = id)
    fotografia_contexto = FotografiaContexto.objects.get(id_plano = id)
    resena_patrimonial = ResenaPatrimonial.objects.get(id_plano = id)
    valoracion_atributos = ValoracionAtributos.objects.get(id_plano = id)
    informacion_tecnica = InformacionTecnica.objects.get(id_plano = id)
    caracteristicas_morfologicas = CaracteristicasMorfologicas.objects.get(id_plano = id)
    estado_de_conservacion = EstadoDeConservacion.objects.get(id_plano = id)
    grado_de_alteracion = GradoDeAlteracion.objects.get(id_plano = id)
    aptitud_de_rehabilitacion = AptitudDeRehabilitacion.objects.get(id_plano = id)
    relacion_del_inmueble_con_el_terreno = RelacionDelInmuebleConElTerreno.objects.get(id_plano = id)
    categoria_de_acuerdo_a_su_uso = CategoriaDeAcuerdoASuUso.objects.get(id_plano = id)
    conclusiones = Conclusiones.objects.get(id_plano = id)
    fuentes_referenciales_y_bibliograficas = FuentesReferencialesYBibliograficas.objects.get(id_plano = id)

    tipologia = Tipologias.objects.get(id_plano_id = id)
    tipo_cubierta = TipoCubierta.objects.get(id_plano_id = id)
    elementos_valor_significativo = ElementosValorSignificativo.objects.get(id_plano_id = id)
    expresion_fachada = ExpresionDeFachada.objects.get(id_plano_id = id)
    continuidad_edificacion = ContinuidadDeEdificacion.objects.get(id_plano_id = id)

    # Sección 6
    total_valor_urbano = valoracion_atributos.valor_urbano_a + valoracion_atributos.valor_urbano_b + valoracion_atributos.valor_urbano_c
    total_valor_arquitecnico = valoracion_atributos.valor_arquitecnico_a + valoracion_atributos.valor_arquitecnico_b + valoracion_atributos.valor_arquitecnico_c
    total_valor_historico = valoracion_atributos.valor_historico_a + valoracion_atributos.valor_historico_b
    total_valor_economico_social = valoracion_atributos.valor_economico_social_a + valoracion_atributos.valor_economico_social_b + valoracion_atributos.valor_economico_social_c
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico_social

    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
        'fotografia_general': fotografia_general,
        'fotografia_contexto': fotografia_contexto,
        'resena_patrimonial': resena_patrimonial,
        'valoracion_atributos': valoracion_atributos,
        'informacion_tecnica': informacion_tecnica,
        'caracteristicas_morfologicas': caracteristicas_morfologicas,
        'estado_de_conservacion': estado_de_conservacion,
        'grado_de_alteracion': grado_de_alteracion,
        'aptitud_de_rehabilitacion': aptitud_de_rehabilitacion,
        'relacion_del_inmueble_con_el_terreno': relacion_del_inmueble_con_el_terreno,
        'categoria_de_acuerdo_a_su_uso': categoria_de_acuerdo_a_su_uso,
        'conclusiones': conclusiones,
        'fuentes_referenciales_y_bibliograficas': fuentes_referenciales_y_bibliograficas,

        'tipologia': tipologia,
        'tipo_cubierta': tipo_cubierta,
        'elementos_valor_significativo': elementos_valor_significativo,
        'expresion_fachada': expresion_fachada,
        'continuidad_edificacion': continuidad_edificacion,

        'total_valor_urbano': total_valor_urbano,
        'total_valor_arquitecnico': total_valor_arquitecnico,
        'total_valor_historico': total_valor_historico,
        'total_valor_economico_social': total_valor_economico_social,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': request.build_absolute_uri('/')[:-1],
    }

    return render(request, 'ficha/ficha_pdf.html', data)

def eliminar(request,id):
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    identificacion_inmueble.delete()
    return redirect('/ficha/ver_fichas')
    
