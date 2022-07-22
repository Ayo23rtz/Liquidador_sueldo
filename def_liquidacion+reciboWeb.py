import sys
import webbrowser

#-----------------liquidador de sueldos-------------------------------
def liquidar(sueldo_base, hora_ext_trab, antiguedad):
#declaro variables en base a ingresos y acreditaciones
    valor_he = (sueldo_base * 0.01) * hora_ext_trab
    valor_ant = (sueldo_base * 0.03) * antiguedad
    sueldo_inc = sueldo_base + valor_he + valor_ant
 
#-------funcion aparte para las deducciones de ganacias!----------------
    def calculo_ganancias(): # problema a resolver- no puedo extraer la funcion ganancias de la del liquidadp
        if sueldo_inc >= 175000:
            ganancias = sueldo_inc * 0.20
        else:
            ganancias = 0
        return ganancias
        
#------------------Declaracion de variables de deduccion---------------
    jubilacion = sueldo_inc * 0.11
    deduccion_ganancias = calculo_ganancias() # -variable contendora de la funcion que calcula ganancias-
    total_deducciones = jubilacion + deduccion_ganancias
    sueldo_total = sueldo_inc - total_deducciones
 
    return [valor_he, valor_ant, jubilacion, deduccion_ganancias, sueldo_total]
 
 
def generar_recibo(nombre_archivo, sueldo_base, horas_extra, antiguedad, jubilacion, ganancias, total):
    html = """<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Recibo de sueldo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
    @media screen {
        @font-face {
        font-family: 'Source Sans Pro';
        font-style: normal;
        font-weight: 400;
        src: local('Source Sans Pro Regular'), local('SourceSansPro-Regular'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/ODelI1aHBYDBqgeIAH2zlBM0YzuT7MdOe03otPbuUS0.woff) format('woff');
        }
        @font-face {
        font-family: 'Source Sans Pro';
        font-style: normal;
        font-weight: 700;
        src: local('Source Sans Pro Bold'), local('SourceSansPro-Bold'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/toadOcfmlt9b38dHJxOBGFkQc6VGVFSmCnC_l7QZG60.woff) format('woff');
        }
    }
    body,
    table,
    td,
    a {
        -ms-text-size-adjust: 100%; /* 1 */
        -webkit-text-size-adjust: 100%; /* 2 */
    }
    table,
    td {
        mso-table-rspace: 0pt;
        mso-table-lspace: 0pt;
    }
    a[x-apple-data-detectors] {
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        color: inherit !important;
        text-decoration: none !important;
    }
    div[style*="margin: 16px 0;"] {
        margin: 0 !important;
    }
    body {
        width: 100% !important;
        height: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    table {
        border-collapse: collapse !important;
    }
    a {
        color: #1a82e2;
    }
    img {
        height: auto;
        line-height: 100%;
        text-decoration: none;
        border: 0;
        outline: none;
    }
    </style>
    </head>
    <body style="background-color: #D2C7BA;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
        <td align="center" bgcolor="#D2C7BA">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
            <tr>
                <td align="left" bgcolor="#ffffff" style="padding: 36px 24px 0; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; border-top: 3px solid #d4dadf;">
                <h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">Recibo de sueldo</h1>
                </td>
            </tr>
            </table>
        </td>
        </tr>
        <tr>
        <td align="center" bgcolor="#D2C7BA">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
            <tr>
                <td align="left" bgcolor="#ffffff" style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                {tabla}
                </td>
            </tr>
            </table>
        </td>
        </tr>
    </table>
    </body>
    </html>
    """
    tabla = """
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
        <td align="left" bgcolor="#D2C7BA" width="75%" style="padding: 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;"><strong>Descripción</strong></td>
        <td align="left" bgcolor="#D2C7BA" width="25%" style="padding: 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;"><strong>Importe</strong></td>
        </tr>
        <tr>
        <td align="left" width="75%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Sueldo base</td>
        <td align="left" width="25%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">${sueldo_base}</td>
        </tr>
        <tr>
        <td align="left" width="75%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Horas extra</td>
        <td align="left" width="25%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">${horas_extra}</td>
        </tr>
        <tr>
        <td align="left" width="75%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Antigüedad</td>
        <td align="left" width="25%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">${antiguedad}</td>
        </tr>
        <tr>
        <td align="left" width="75%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Jubilación</td>
        <td align="left" width="25%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">${jubilacion}</td>
        </tr>
        <tr>
            <td align="left" width="75%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Ganancias</td>
            <td align="left" width="25%" style="padding: 6px 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">${ganancias}</td>
        </tr>
        <tr>
        <td align="left" width="75%" style="padding: 12px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; border-top: 2px dashed #D2C7BA; border-bottom: 2px dashed #D2C7BA;"><strong>Total</strong></td>
        <td align="left" width="25%" style="padding: 12px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; border-top: 2px dashed #D2C7BA; border-bottom: 2px dashed #D2C7BA;"><strong>${total}</strong></td>
        </tr>
    </table>
    """
    with open(nombre_archivo, "w", encoding="utf8") as f:
        f.write(
            html.replace(
                "{tabla}",
                tabla.format(
                    sueldo_base=sueldo_base,
                    horas_extra=horas_extra,
                    antiguedad=antiguedad,
                    jubilacion=jubilacion,
                    ganancias=ganancias,
                    total=total
                )
            )
        )
#************************************************************************
#---------Ingreso de datos-------------------------------------------
sueldo_base = (input('Ingrese su sueldo base: '))
print('PROGRAMA DE LIQUIDACION DE SUELDOS')

if not sueldo_base.isdecimal():
    print ('Ud. a ingresado un caracter no valido.')
    sys.exit()
 
sueldo_base = float(sueldo_base)
if sueldo_base < 1:
    print ('El monto de su sueldo no es valido.')
    sys.exit()
 
hora_ext_trab = input('Ingrese las horas extras trabajadas este mes: ')
if not hora_ext_trab.isdecimal():
    print ('Ud. a ingresado un caracter no valido.')
    sys.exit()
 
hora_ext_trab = float(hora_ext_trab)
 
antiguedad = (input('Ingrese su antiguedad en anios: '))
if not antiguedad.isdecimal():
    print ('Ud. a ingresado un caracter no valido.') 
    sys.exit()
 
antiguedad = float(antiguedad) 

#*********************************************************************************** 
#------------------Llamado a la funcion --------------------------------
liquidacion = liquidar(sueldo_base, hora_ext_trab, antiguedad)


#------------Declaro variables del recibo------------------------------
# Acá guardo en variables distintas los elementos de la lista
# que retornó la función liquidar()
# También se podría hacer en una línea así:
# adicional_horas_extra, adicional_antiguedad, deduccion_jubilacion, deduccion_ganancias, sueldo_total = liquidacion
adicional_horas_extra = liquidacion[0]
adicional_antiguedad = liquidacion[1]
deduccion_jubilacion = liquidacion[2]
deduccion_ganancias = liquidacion[3]
sueldo_total = liquidacion[4]

#-------------Llamo a la funcion generar recibo------------------------------
# Luego le paso los datos de esas variables a los argumentos para generar el recibo.
generar_recibo(
    "recibo.html",
    sueldo_base,
    adicional_horas_extra,
    adicional_antiguedad,
    deduccion_jubilacion,
    deduccion_ganancias,
    sueldo_total
)

#-------------Abro el recibo automaticamente en una pagina del navegador por defecto-----
webbrowser.open_new_tab('file:///Users/ayelenmiserez/Documents/Formacion/PROGRAMACION/EDUCACION%20IT/PHYTON/PYTHON_PNP2/CLASE%205/recibo.html')


