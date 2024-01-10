from io import BytesIO, StringIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings

def save_pdf(params):
    template = get_template('ficha/ficha_pdf.html')
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    file_name = uuid.uuid4()

    try:
        with open(str(settings.BASE_DIR) + '/media/' + str(file_name) + '.pdf', 'wb+') as f:
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

    except Exception as e:
        print("-------------------")
        print(e)
        print("-------------------")

    if pdf.err:
        return '', False
    return file_name, True

def save_pdf_2(params, filename):
    template = get_template('ficha/ficha_pdf_2.html')
    html = template.render(params)
    # file_name = str(uuid.uuid4())
    file_name = filename
    output_filename = str(settings.BASE_DIR) + '/media/' + str(file_name) + '.pdf'
    
    try: 
        resultFile = open(output_filename, "w+b")

        # convert HTML to PDF
        pisaStatus = pisa.CreatePDF(html, dest=resultFile, encoding='utf-8', show_error_as_pdf=True, debug=True)

        print("ººººººººººººººººº")
        print(pisaStatus.error("Error"))
        print("ººººººººººººººººº")

        # close output file
        resultFile.close()
    except Exception as e:
        print("-------------------")
        print(e)
        print("-------------------")

    return output_filename, pisaStatus.error
def save_pdf_3(params, filename):
    template = get_template('ficha/tabla_valoracion.html')
    html = template.render(params)
    # file_name = str(uuid.uuid4())
    file_name = filename
    output_filename = str(settings.BASE_DIR) + '/media/' + str(file_name) + '.pdf'
    
    try: 
        resultFile = open(output_filename, "w+b")

        # convert HTML to PDF
        pisaStatus = pisa.CreatePDF(html, dest=resultFile, encoding='utf-8', show_error_as_pdf=True, debug=True)

        print("ººººººººººººººººº")
        print(pisaStatus.error("Error"))
        print("ººººººººººººººººº")

        # close output file
        resultFile.close()
    except Exception as e:
        print("-------------------")
        print(e)
        print("-------------------")

    return output_filename, pisaStatus.error

# AVECES LA VIDA DE REALMENTE PIENSO QU
# NOTA DEL POGRAMADOR : SI USTED ESTA AQUÍ ES QUE NOSOTROS YA NO ESTOY EN LA EMPRESAS POR ENDE ES TU RESPONSABILIDAD AHORA CAE EN TI 
# CASI NADIE MIRA EL CÓDIGO PORQUE REALMENTE NO REVISAN EL DESARROLLO SOLO MIRA EL RESULTADO ENTONCES CUALQUIER TIPO DE NOTA DEJARLA AQUÍ
# TE RECOMIENDO PACIENCIA Y NO REALIZAR LA COSAS COMO SI FUERA PARA AYER YA QUE ESO TE DEJARAS EN ESTÁNDARES ALTOS Y TE VAN A PEDIR COSAS EN MENOR TIEMPO.
# SOY EL POGRAMADOR: 1