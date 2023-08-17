from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings
from pyproj import Proj, transform 
from .helpers import save_pdf, save_pdf_2
from datetime import datetime
from datetime import date
from django.http import JsonResponse,HttpResponseBadRequest


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
    last_id =  IdentificacionInmueble.objects.latest('id_plano').__int__
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
    data = {'OPTIONS': OPTIONS,
            'id_plano':last_id}
    if request.method == 'POST':
        # Sección 1
        rol = request.POST['rol']
        unidad_vecinal = request.POST['unidad_vecinal']
        region = request.POST['region']
        comuna = request.POST['comuna']
        calle = request.POST['calle']
        numero = request.POST['numero']
        plan_cerro_poblacion = request.POST['plan_cerro_poblacion']
        denominacion_inmueble = request.POST['denominacion_inmueble']
        
        autor = request.POST['autor']
        identificacioninmueble  = IdentificacionInmueble.objects.create(
                                              rol = rol,
                                              unidad_vecinal = unidad_vecinal,
                                              region = region,
                                              comuna = comuna,
                                              calle = calle,
                                              numero = numero,
                                              plan_cerro_poblacion = plan_cerro_poblacion,
                                              denominacion_inmueble = denominacion_inmueble,
                                              autor = autor,
                                              usuario = request.user)
        # Sección 2
        try: 
            imagen_plano = request.FILES['imagen_plano']
        except:
            imagen_plano = ""
        if request.POST['latitud'] == "0" and request.POST['longitud'] == "0":
            longitud = 0
            latitud = 0
        else:
            longitud = request.POST['longitud']
            latitud = request.POST['latitud']

        planoubicacion = PlanoUbicacion.objects.create(id_plano = identificacioninmueble,
                                      imagen_plano = imagen_plano,
                                      latitud = latitud,
                                      longitud = longitud)
        # Sección 3
        try: 
            imagen_fotografia = request.FILES['imagen_fotografia']
        except:
            imagen_fotografia = ""
        fotografiageneral = FotografiaGeneral.objects.create(id_plano = identificacioninmueble,
                                        imagen_fotografia = imagen_fotografia)
        
        # Sección 4

        try:
            registro_fotografico_1 = request.FILES['registro_fotografico_1']
        except:
            registro_fotografico_1 = ""
        try:
            registro_fotografico_2 = request.FILES['registro_fotografico_2']
        except:
            registro_fotografico_2 = ""
            
        
        FotografiaContexto.objects.create(id_plano = identificacioninmueble,
                                          registro_fotografico_1 = registro_fotografico_1,
                                          registro_fotografico_2 = registro_fotografico_2)
        # Sección 5

        valor_urbano = request.POST['valor_urbano']
        valor_arquitecnico = request.POST['valor_arquitecnico']
        valor_historico = request.POST['valor_historico']
        valor_economico = request.POST['valor_economico']
        valor_social = request.POST['valor_social']

        ResenaPatrimonial.objects.create(id_plano = identificacioninmueble,
                                         valor_urbano = valor_urbano,
                                         valor_arquitecnico = valor_arquitecnico,
                                         valor_historico = valor_historico,
                                         valor_economico = valor_economico,
                                         valor_social = valor_social)
        # Sección 6
        
        valor_urbano_a = request.POST['valor_urbano_a']
        valor_urbano_b = request.POST['valor_urbano_b']
        valor_urbano_c = request.POST['valor_urbano_c']

        valor_arquitecnico_a = request.POST['valor_arquitecnico_a']
        valor_arquitecnico_b  = request.POST['valor_arquitecnico_b']
        valor_arquitecnico_c  = request.POST['valor_arquitecnico_c']

        valor_historico_a = request.POST['valor_historico_a']
        valor_historico_b = request.POST['valor_historico_b']
        valor_historico_c = request.POST['valor_historico_c']

        valor_economico_a = request.POST['valor_economico_a']
        valor_economico_b = request.POST['valor_economico_b']
        

        valor_social_a = request.POST['valor_social_a']
       
        zona_de_conservacion = request.POST['zona_de_conservacion']
        identificacion_zch = request.POST['identificacion_zch']
        
        ValoracionAtributos.objects.create(id_plano = identificacioninmueble,
                                           valor_arquitecnico_a = valor_arquitecnico_a,
                                           valor_arquitecnico_b = valor_arquitecnico_b,
                                           valor_arquitecnico_c = valor_arquitecnico_c,
                                           valor_urbano_a = valor_urbano_a,
                                           valor_urbano_c = valor_urbano_c,
                                           valor_urbano_b = valor_urbano_b,
                                           valor_historico_a = valor_historico_a,
                                           valor_historico_b = valor_historico_b,
                                           valor_historico_c = valor_historico_c,
                                           valor_economico_a = valor_economico_a,
                                           valor_economico_b = valor_economico_b,
                                           
                                           valor_social_a = valor_social_a,
                                       
                                           zona_de_conservacion = zona_de_conservacion,
                                           identificacion_zch = identificacion_zch)

        # Sección 7 
        piso_original_subterraneo = request.POST['piso_original_subterraneo']
        piso_original_primer_piso  = request.POST['piso_original_primer_piso']
        piso_original_pisos_superiores  = request.POST['piso_original_pisos_superiores']
        piso_actual_subterraneo  = request.POST['piso_actual_subterraneo']
        piso_actual_primer_piso   = request.POST['piso_actual_primer_piso']
        piso_actual_pisos_superiores   = request.POST['piso_actual_pisos_superiores']

        anio_construccion = request.POST['anio_construccion']

        tipo_propiedad = request.POST['tipo_propiedad']
        tipo_usuario = request.POST['tipo_usuario']

        regimen_propiedad = request.POST['regimen_propiedad'] 
        
        afectacion_actual = request.POST['afectacion_actual'] 

        observaciones = request.POST['informacion_tecnica_observaciones']
        InformacionTecnica.objects.create(piso_original_subterraneo = piso_original_subterraneo,
                                          piso_original_primer_piso = piso_original_primer_piso,
                                          piso_original_pisos_superiores = piso_original_pisos_superiores,
                                          piso_actual_subterraneo = piso_actual_subterraneo,
                                          piso_actual_primer_piso = piso_actual_primer_piso,
                                          piso_actual_pisos_superiores = piso_actual_pisos_superiores,
                                          anio_construccion = anio_construccion,
                                          tipo_propiedad = tipo_propiedad,
                                          tipo_usuario = tipo_usuario,
                                          regimen_propiedad = regimen_propiedad,
                                          afectacion_actual = afectacion_actual,
                                          observaciones = observaciones,
                                          id_plano = identificacioninmueble)
        # Sección 8
        print( request.POST.get('manzana'))
        if  request.POST.get('manzana'):
            manzana = True
        else:
            manzana = False

        if  request.POST.get('esquina'):
            esquina  = True
        else:
            esquina  = False

        if  request.POST.get('entre_medianeros'):
            entre_medianeros  = True
        else:
            entre_medianeros  = False

        if  request.POST.get('cabezal'):
            cabezal = True
        else:
            cabezal = False

        if  request.POST.get('crucero'):
            crucero = True
        else:
            crucero = False
        if  request.POST.get('doble_frente'):
            doble_frente  = True
        else:
            doble_frente  = False
        if  request.POST.get('antejardines'):
            antejardines   = True
        else:
            antejardines   = False

        tipologia = Tipologias.objects.create(id_plano = identificacioninmueble,
                                  manzana = manzana,
                                  esquina = esquina,
                                  cabezal = cabezal,
                                  crucero = crucero,
                                  entre_medianeros = entre_medianeros,
                                  doble_frente = doble_frente,
                                  antejardines = antejardines)

        if  request.POST.get('horizontal'):
            horizontal  = True
        else:
            horizontal  = False

        if  request.POST.get('inclinada'):
            inclinada   = True
        else:
            inclinada   = False

        if  request.POST.get('curva'):
            curva   = True
        else:
            curva   = False

        if  request.POST.get('tipo_cubierta_otro'):
            otro = True
        else:
            otro = False
        otro_texto  = request.POST['tipo_cubierta_otro_texto']


        tipocubierta = TipoCubierta.objects.create(id_plano = identificacioninmueble,
                                  horizontal = horizontal,
                                  inclinada = inclinada,
                                  curva = curva,
                                  otro = otro,
                                  otro_texto = otro_texto)
        
        
        if  request.POST.get('cornisamientos'):
            cornisamientos  = True
        else:
            cornisamientos  = False

        if  request.POST.get('zocalos'):
            zocalos   = True
        else:
            zocalos   = False

        if  request.POST.get('molduras_relevantes_en_yeso'):
            molduras_relevantes_en_yeso    = True
        else:
            molduras_relevantes_en_yeso    = False

        if  request.POST.get('ornamentacion_en_madera'):
            ornamentacion_en_madera  = True
        else:
            ornamentacion_en_madera  = False

        if  request.POST.get('remate_en_techumbre'):
            remate_en_techumbre = True
        else:
            remate_en_techumbre = False

        if  request.POST.get('elementos_valor_significativo_otro'):
            otro_v = True
        else:
            otro_v = False
        otro_texto_v = request.POST['elementos_valor_significativo_otro_texto']

        elementosvalorsignificativo = ElementosValorSignificativo.objects.create(id_plano = identificacioninmueble,
                                                   cornisamientos = cornisamientos,
                                                   zocalos = zocalos,
                                                   molduras_relevantes_en_yeso = molduras_relevantes_en_yeso,
                                                   ornamentacion_en_madera = ornamentacion_en_madera,
                                                   remate_en_techumbre = remate_en_techumbre,
                                                   otro = otro_v,
                                                   otro_texto = otro_texto_v
                                                   
        )

        if  request.POST.get('lenguaje_de_vanos_comun'):
            lenguaje_de_vanos_comun    = True
        else:
            lenguaje_de_vanos_comun    = False

        if  request.POST.get('simetria'):
            simetria    = True
        else:
            simetria    = False

        if  request.POST.get('modulacion_en_serie'):
            modulacion_en_serie  = True
        else:
            modulacion_en_serie  = False

        if  request.POST.get('torreon_en_esquina'):
            torreon_en_esquina = True
        else:
            torreon_en_esquina = False

        if  request.POST.get('elementos_valor_significativo_otro'):
            elementos_valor_significativo = True
        else:
            elementos_valor_significativo = False
        otro_texto_elementos_valor_significativ = request.POST['elementos_valor_significativo_otro_texto']

        expresiondefachada = ExpresionDeFachada.objects.create(id_plano = identificacioninmueble,
                                                               lenguaje_de_vanos_comun = lenguaje_de_vanos_comun,
                                                                modulacion_en_serie = modulacion_en_serie,
                                                                simetria = simetria,
                                                                otro = elementos_valor_significativo,
                                                                otro_texto = otro_texto_elementos_valor_significativ,
                                                                torreon_en_esquina = torreon_en_esquina
        )
        if  request.POST.get('fachada'):
            fachada   = True
        else:
            fachada   = False
        
        if  request.POST.get('linea_de_remate_superior'):
                linea_de_remate_superior    = True
        else:
                linea_de_remate_superior    = False

        if request.POST.get('linea_de_zocalo_escalonado'):
            linea_de_zocalo_escalonado = True
        else:
            linea_de_zocalo_escalonado = False

        if  request.POST.get('linea_de_zocalo_continuo'):
            linea_de_zocalo_continuo    = True
        else:
            linea_de_zocalo_continuo    = False
        if  request.POST.get('linea_de_zocalo_continuo'):
            linea_de_zocalo_continuo    = True
        else:
            linea_de_zocalo_continuo    = False
        if  request.POST.get('realce_horizontal_prodominante'):
            realce_horizontal_prodominante  = True
        else:
            realce_horizontal_prodominante  = False

        if  request.POST.get('zocalo_de_mamposteria'):
            zocalo_de_mamposteria = True
        else:
            zocalo_de_mamposteria = False

        if  request.POST.get('continuidad_edificacion_otro'):
            otro  = True
        else:
            otro  = False

        otro_texto = request.POST['continuidad_edificacion_otro_texto']

        continuidaddeedificacion = ContinuidadDeEdificacion.objects.create(id_plano = identificacioninmueble,
                                                                            fachada = fachada,
                                                                            linea_de_zocalo_escalonado = linea_de_zocalo_escalonado,
                                                                            linea_de_remate_superior = linea_de_remate_superior,
                                                                            linea_de_zocalo_continuo = linea_de_zocalo_continuo,
                                                                            realce_horizontal_prodominante = realce_horizontal_prodominante,
                                                                            zocalo_de_mamposteria = zocalo_de_mamposteria,
                                                                            otro = otro,
                                                                            otro_texto =otro_texto,
        )
        sistema_agrupamiento = request.POST['sistema_agrupamiento']
        volumetria = request.POST['volumetria']
        observaciones =request.POST['caracteristicas_morfologicas_observaciones']
        try:
            fotografia_valor_significativo  = request.FILES['fotografia_valor_significativo']
        except:
            fotografia_valor_significativo = ""

        try:
            fotografia_expresion_fachada   = request.FILES['fotografia_expresion_fachada']
        except:
            fotografia_expresion_fachada  = ""

        try:
            fotografia_expresion_fachada   = request.FILES['fotografia_expresion_fachada']
        except:
            fotografia_expresion_fachada  = ""

        try:
            fotografia_detalles_constructivos  = request.FILES['fotografia_detalles_constructivos']
        except:
            fotografia_detalles_constructivos  = ""

        try:
            fotografia_contexto_1  = request.FILES['fotografia_contexto_1']
        except:
            fotografia_contexto_1  = ""

        try:
            fotografia_contexto_2  = request.FILES['fotografia_contexto_2']
        except:
            fotografia_contexto_2  = ""

        try:
            fotografia_contexto_3  = request.FILES['fotografia_contexto_3']
        except:
            fotografia_contexto_3  = ""



        terreno = request.POST['terreno']
        edificada = request.POST['edificada']
        protegida = request.POST['protegida']
        altura_en_pisos = request.POST['altura_en_pisos']
        altura_en_metros = request.POST['altura_en_metros']
        antejardin_frente_1 = request.POST['antejardin_frente_1']
        antejardin_frente_2 = request.POST['antejardin_frente_2']

        materialidad_estructura = request.POST['materialidad_estructura']
        materialidad_cubierta = request.POST['materialidad_cubierta']
        if request.POST.get('materialidad_revestimientos') == "OTRO":
            materialidad_revestimientos =  request.POST['materialidad_revestimientos_text']
        else:
            materialidad_revestimientos =  request.POST['materialidad_revestimientos']
        descripcion_del_inmubebles= request.POST['descripcion_del_inmubebles']

        CaracteristicasMorfologicas.objects.create(id_plano = identificacioninmueble,
                                                   tipologia = tipologia,
                                                   sistema_agrupamiento = sistema_agrupamiento,
                                                   tipo_cubierta = tipocubierta,
                                                   volumetria = volumetria,
                                                   elementos_valor_significativo = elementosvalorsignificativo,
                                                   expresion_de_fachada = expresiondefachada,
                                                   continuidad_de_edificacion = continuidaddeedificacion,
                                                   observaciones = observaciones,
                                                   fotografia_valor_significativo = fotografia_valor_significativo,
                                                   fotografia_expresion_fachada = fotografia_expresion_fachada,
                                                   fotografia_detalles_constructivos = fotografia_detalles_constructivos,
                                                   fotografia_contexto_1 = fotografia_contexto_1,
                                                   fotografia_contexto_2 = fotografia_contexto_2,
                                                   fotografia_contexto_3 = fotografia_contexto_3,
                                                   terreno = terreno,
                                                   edificada = edificada,
                                                   protegida = protegida,
                                                   altura_en_pisos = altura_en_pisos,
                                                   altura_en_metros = altura_en_metros,
                                                   antejardin_frente_1 = antejardin_frente_1,
                                                   antejardin_frente_2 = antejardin_frente_2,
                                                   materialidad_estructura = materialidad_estructura,
                                                   materialidad_cubierta = materialidad_cubierta,
                                                   materialidad_revestimientos = materialidad_revestimientos,
                                                   descripcion_del_inmubebles = descripcion_del_inmubebles)
    # Sección 9
        inmueble = request.POST['inmueble']
        entorno = request.POST['entorno']

        EstadoDeConservacion.objects.create(id_plano = identificacioninmueble,
                                            inmueble = inmueble,
                                            entorno = entorno)
    # Sección 10
        fachada = request.POST['grado_de_alteracion_fachada']
        cubierta = request.POST['grado_de_alteracion_cubierta']

        GradoDeAlteracion.objects.create(id_plano = identificacioninmueble,
                                            fachada = fachada,
                                            cubierta = cubierta
        )

        # Seccion 11
        if  request.POST.get('vivienda'):
            vivienda   = True
        else:
            vivienda   = False
        if  request.POST.get('equipamiento'):
            equipamiento     = True
        else:
            equipamiento     = False
        if  request.POST.get('comercio'):
            comercio     = True
        else:
            comercio     = False
        if  request.POST.get('aptitud_de_rehabilitacion_otro'):
            otro = True
        else:
            otro = False
        otro_texto = request.POST['aptitud_de_rehabilitacion_otro_texto']

        AptitudDeRehabilitacion.objects.create(id_plano = identificacioninmueble,
                                                vivienda = vivienda,
                                                equipamiento = equipamiento,
                                                comercio = comercio,
                                                otro = otro,
                                                otro_texto = otro_texto
        )
        # Seccion 12
        if request.POST.get('imagen_urbana_relevante_por_ubicacion'):
            imagen_urbana_relevante_por_ubicacion = True
        else: 
            imagen_urbana_relevante_por_ubicacion = False

        if request.POST.get('imagen_urbana_relevante_por_singularidad'):
            imagen_urbana_relevante_por_singularidad = True
        else: 
            imagen_urbana_relevante_por_singularidad = False

        if request.POST.get('forma_parte_de_un_conjunto'):
            forma_parte_de_un_conjunto = True
        else: 
            forma_parte_de_un_conjunto = False

        espacio_publico = request.POST['espacio_publico']
        # relacion_del_inmueble_con_el_terreno.monumentos_historicos = request.POST.get('monumentos_historicos')
        # relacion_del_inmueble_con_el_terreno.inmuebles_conservacion_historica = request.POST.get('inmuebles_conservacion_historica')

        # 12.5 Monumentos históricos
        if request.POST.get('mon_his_predio_contiguo'):
            mon_his_predio_contiguo = True
        else:
            mon_his_predio_contiguo =  False 

        if request.POST.get('mon_his_manzana'):
            mon_his_manzana = True
        else:
            mon_his_manzana =  False 

        if request.POST.get('mon_his_manzana_enfrente'):
            mon_his_manzana_enfrente = True
        else:
            mon_his_manzana_enfrente =  False 

        if request.POST.get('mon_his_relacion_visual'):
            mon_his_relacion_visual = True
        else:
            mon_his_relacion_visual =  False 

        # 12.5 Inmuebles de conservación histórica
        if request.POST.get('inm_con_his_predio_contiguo'):
            inm_con_his_predio_contiguo = True
        else:
            inm_con_his_predio_contiguo =  False 

        if request.POST.get('inm_con_his_manzana_enfrente'):
            inm_con_his_manzana_enfrente = True
        else:
            inm_con_his_manzana_enfrente =  False 
        
        if request.POST.get('inm_con_his_relacion_visual'):
            inm_con_his_relacion_visual = True
        else:
            inm_con_his_relacion_visual =  False 

        if request.POST.get('inm_con_his_manzana'):
            inm_con_his_manzana = True
        else:
            inm_con_his_manzana =  False 

        observaciones = request.POST['espacio_publico_observaciones']
        Otros_elementos_patrimonial = request.POST['Otros_elementos_patrimonial']
        RelacionDelInmuebleConElTerreno.objects.create(id_plano = identificacioninmueble,
                                                       imagen_urbana_relevante_por_ubicacion = imagen_urbana_relevante_por_ubicacion,
                                                       imagen_urbana_relevante_por_singularidad = imagen_urbana_relevante_por_singularidad,
                                                       forma_parte_de_un_conjunto = forma_parte_de_un_conjunto,
                                                       espacio_publico = espacio_publico,
                                                       mon_his_predio_contiguo = mon_his_predio_contiguo,
                                                       mon_his_manzana = mon_his_manzana,
                                                       mon_his_manzana_enfrente = mon_his_manzana_enfrente,
                                                       mon_his_relacion_visual = mon_his_relacion_visual,
                                                       inm_con_his_predio_contiguo = inm_con_his_predio_contiguo,
                                                       inm_con_his_manzana = inm_con_his_manzana,
                                                       inm_con_his_manzana_enfrente= inm_con_his_manzana_enfrente,
                                                       inm_con_his_relacion_visual = inm_con_his_relacion_visual,
                                                       observaciones = observaciones,
                                                       Otros_elementos_patrimonial = Otros_elementos_patrimonial
        )
        # Seccion 13
        observaciones = request.POST['categoria_acuerdo_uso']
        CategoriaDeAcuerdoASuUso.objects.create(id_plano = identificacioninmueble,
                                                observaciones = observaciones)
        
        # Seccion 14
        conclusiones = request.POST['conclusiones']
        Conclusiones.objects.create(id_plano = identificacioninmueble,
                                    conclusiones = conclusiones)
        
        # Seccion 15
        fuentes_referenciales_y_bibliograficas  = request.POST['fuentes_referenciales_y_bibliograficas']
        FuentesReferencialesYBibliograficas.objects.create(id_plano = identificacioninmueble,
                                                    fuentes_referenciales_y_bibliograficas = fuentes_referenciales_y_bibliograficas)
        
        extra  = request.POST['observacion']

        
        return redirect('/ficha/ver_fichas')
    return render(request, 'ficha/crear_ficha.html',data)

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
    extra = observacion.objects.get(id_plano_id = id)

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
    total_valor_historico = valoracion_atributos.valor_historico_a + valoracion_atributos.valor_historico_b + valoracion_atributos.valor_historico_c
    total_valor_economico = valoracion_atributos.valor_economico_a + valoracion_atributos.valor_economico_b 
    total_valor_social = valoracion_atributos.valor_social_a 
    
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico + total_valor_social
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
        resena_patrimonial.valor_economico = request.POST.get('valor_economico')
        resena_patrimonial.valor_social = request.POST.get('valor_economico')
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
        valoracion_atributos.valor_historico_c = request.POST.get('valor_historico_c')

        valoracion_atributos.valor_economico_a = request.POST.get('valor_economico_a')
        valoracion_atributos.valor_economico_b = request.POST.get('valor_economico_b')
        

        valoracion_atributos.valor_social_a = request.POST.get('valor_social_a')
        
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

        if request.FILES.get('fotografia_contexto_1'):
            caracteristicas_morfologicas.fotografia_contexto_1 = request.FILES.get('fotografia_contexto_1')

        if request.FILES.get('fotografia_contexto_2'):
            caracteristicas_morfologicas.fotografia_contexto_2 = request.FILES.get('fotografia_contexto_2')

        if request.FILES.get('fotografia_contexto_3'):
            caracteristicas_morfologicas.fotografia_contexto_3 = request.FILES.get('fotografia_contexto_3')

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
        
        extra.descripcion = request.POST.get('observacion')
        extra.save()

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
        'observacion':extra,
        'tipologia': tipologia,
        'tipo_cubierta': tipo_cubierta,
        'elementos_valor_significativo': elementos_valor_significativo,
        'expresion_fachada': expresion_fachada,
        'continuidad_edificacion': continuidad_edificacion,

        'OPTIONS': OPTIONS,

        'total_valor_urbano': total_valor_urbano,
        'total_valor_arquitecnico': total_valor_arquitecnico,
        'total_valor_historico': total_valor_historico,
        'total_valor_economico': total_valor_economico,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'ficha/editar_ficha.html', data)

@login_required(login_url='/login/')
def ver_fichas(request):
    if request.user.is_staff:
        identificacion_inmueble = IdentificacionInmueble.objects.all()
    else:
        identificacion_inmueble = IdentificacionInmueble.objects.filter(usuario=request.user)



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
    total_valor_economico = valoracion_atributos.valor_economico_a + valoracion_atributos.valor_economico_b 
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico + valoracion_atributos.valor_urbano_a

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
        'total_valor_economico': total_valor_economico,
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
    total_valor_economico = valoracion_atributos.valor_economico_a + valoracion_atributos.valor_economico_b + valoracion_atributos.valor_economico_c
    total_valoracion = total_valor_urbano + total_valor_arquitecnico + total_valor_historico + total_valor_economico

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
        'total_valor_economico': total_valor_economico,
        'total_valoracion': total_valoracion,

        'MEDIA_URL': request.build_absolute_uri('/')[:-1],
    }

    return render(request, 'ficha/ficha_pdf.html', data)

def eliminar(request,id):
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    identificacion_inmueble.delete()
    return redirect('/ficha/ver_fichas')

@login_required(login_url='/login/')
def get_location(request):
    if request.method == 'POST':
        print(request.POST['latitud'])
        print(request.POST['longitud'])
        lat = float(request.POST['latitud'])
        lon = float(request.POST['longitud'])

        in_proj = Proj(init='epsg:4326')  # sistema de coordenadas geográficas
        out_proj = Proj(init='epsg:32719')  # sistema de coordenadas UTM (zona 19)

        easting, northing = transform(in_proj, out_proj, lon, lat)

        # redondeamos las coordenadas a dos decimales
        easting = round(easting, 2)
        northing = round(northing, 2)

        # creamos un diccionario con las coordenadas redondeadas
        response_data = {
            'easting': easting,
            'northing': northing
        }

        # devolvemos la respuesta en formato JSON
        return JsonResponse(response_data)
    return HttpResponseBadRequest('La petición no es válida.')
