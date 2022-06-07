
#  ============================================================================
#   By  Ruben Pantaleon Miranda | rpm+                         EPSON Argentina
#  ============================================================================


# It requires pywin32:  https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
#
# Note: windll use by default the calling convention "StdCall"
import ctypes
from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer
import binascii
import sys
# from ctypes import windll


# -----------------------------------------------------------------------------
# GLOBAL DEFINES AREA
# -----------------------------------------------------------------------------
ID_TIPO_COMPROBANTE_TIQUET                = c_int( 1 ).value  # "83"  Tique
ID_TIPO_COMPROBANTE_TIQUE_FACTURA         = c_int( 2 ).value  # "81"  Tique Factura A, "82" Tique Factura B, "111" Tique Factura C, "118" Tique Factura M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO = c_int( 3 ).value  # "110" Tique Nota de Credito, "112" Tique Nota de Credito A, "113" Tique Nota de Credito B, "114" Tique Nota de Credito C, "119" Tique Nota de Credito M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO  = c_int( 4 ).value  # "115" Tique Nota de Debito A, "116" Tique Nota de Debito B, "117" Tique Nota de Debito C, "120" Tique Nota de Debito M

ID_TIPO_DOCUMENTO_NINGUNO           = c_int( 0 ).value
ID_TIPO_DOCUMENTO_DNI               = c_int( 1 ).value
ID_TIPO_DOCUMENTO_CUIL              = c_int( 2 ).value
ID_TIPO_DOCUMENTO_CUIT              = c_int( 3 ).value
ID_TIPO_DOCUMENTO_CEDULA_IDENTIDAD  = c_int( 4 ).value
ID_TIPO_DOCUMENTO_PASAPORTE         = c_int( 5 ).value
ID_TIPO_DOCUMENTO_LIB_CIVICA        = c_int( 6 ).value
ID_TIPO_DOCUMENTO_LIB_ENROLAMIENTO  = c_int( 7 ).value

ID_RESPONSABILIDAD_IVA_NINGUNO                              = c_int(  0 ).value
ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO                = c_int(  1 ).value
ID_RESPONSABILIDAD_IVA_NO_RESPONSABLE                       = c_int(  3 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA                       = c_int(  4 ).value
ID_RESPONSABILIDAD_IVA_CONSUMIDOR_FINAL                     = c_int(  5 ).value
ID_RESPONSABILIDAD_IVA_EXENTO                               = c_int(  6 ).value
ID_RESPONSABILIDAD_IVA_NO_CATEGORIZADO                      = c_int(  7 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA_SOCIAL                = c_int(  8 ).value
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL               = c_int(  9 ).value
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL_SOCIAL        = c_int( 10 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTO_INDEPENDIENTE_PROMOVIDO  = c_int( 11 ).value

ID_MODIFICADOR_AGREGAR_ITEM                     = c_int( 200 ).value
ID_MODIFICADOR_ANULAR_ITEM                      = c_int( 201 ).value
ID_MODIFICADOR_AGREGAR_ITEM_RETORNO_ENVASES     = c_int( 202 ).value
ID_MODIFICADOR_ANULAR_ITEM_RETORNO_ENVASES      = c_int( 203 ).value
ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION        = c_int( 204 ).value
ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION         = c_int( 205 ).value
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO           = c_int( 206 ).value
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO            = c_int( 207 ).value
ID_MODIFICADOR_AGREGAR_ITEM_ANTICIPO            = c_int( 208 ).value
ID_MODIFICADOR_ANULAR_ITEM_ANTICIPO             = c_int( 209 ).value
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO_ANTICIPO  = c_int( 210 ).value
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO_ANTICIPO   = c_int( 211 ).value
ID_MODIFICADOR_DESCUENTO                        = c_int( 400 ).value
ID_MODIFICADOR_AJUSTE                           = c_int( 401 ).value
ID_MODIFICADOR_AJUSTE_NEGATIVO                  = c_int( 402 ).value
ID_MODIFICADOR_AUDITORIA_DETALLADA              = c_int( 500 ).value
ID_MODIFICADOR_AUDITORIA_RESUMIDA               = c_int( 501 ).value

ID_MODIFICADOR_AGREGAR                          = ID_MODIFICADOR_AGREGAR_ITEM
ID_MODIFICADOR_ANULAR                           = ID_MODIFICADOR_ANULAR_ITEM

ID_TASA_IVA_NINGUNO = c_int( 0 ).value
ID_TASA_IVA_EXENTO  = c_int( 1 ).value
ID_TASA_IVA_10_50   = c_int( 4 ).value
ID_TASA_IVA_21_00   = c_int( 5 ).value
ID_TASA_IVA_27_00   = c_int( 6 ).value

ID_IMPUESTO_NINGUNO            = c_int( 0 ).value
ID_IMPUESTO_INTERNO_FIJO       = c_int( 1 ).value
ID_IMPUESTO_INTERNO_PORCENTUAL = c_int( 2 ).value

ID_CODIGO_INTERNO = c_int( 1 ).value
ID_CODIGO_MATRIX  = c_int( 2 ).value

AFIP_CODIGO_UNIDAD_MEDIDA_SIN_DESCRIPCION            = c_int(  0 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO                  = c_int(  1 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METROS                     = c_int(  2 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUADRADO             = c_int(  3 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUBICO               = c_int(  4 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_LITROS                     = c_int(  5 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD                     = c_int(  7 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PAR                        = c_int(  8 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_DOCENA                     = c_int(  9 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_QUILATE                    = c_int( 10 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILLAR                     = c_int( 11 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_ANTIB     = c_int( 12 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD_INT_ACT_INMUNG      = c_int( 13 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO                      = c_int( 14 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO                  = c_int( 15 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO_CUBICO           = c_int( 16 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO                  = c_int( 17 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOLITRO                 = c_int( 18 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_UNIDAD_INT_ACT_INMUNG = c_int( 19 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO                 = c_int( 20 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_ACTIVO           = c_int( 21 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_ACTIVO               = c_int( 22 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_BASE                 = c_int( 23 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTHOR                   = c_int( 24 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_JGO_PQT_MAZO_NAIPES        = c_int( 25 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTHOR                  = c_int( 26 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO_CUBICO          = c_int( 27 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTANT                   = c_int( 28 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_TONELADA                   = c_int( 29 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_DECAMETRO_CUBICO           = c_int( 30 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOMETRO_CUBICO          = c_int( 31 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO_CUBICO           = c_int( 32 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MICROGRAMO                 = c_int( 33 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_NANOGRAMO                  = c_int( 34 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PICOGRAMO                  = c_int( 35 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTANT                  = c_int( 36 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTIG                    = c_int( 37 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIGRAMO                  = c_int( 41 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILILITRO                  = c_int( 47 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CURIE                      = c_int( 48 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILICURIE                  = c_int( 49 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MICROCURIE                 = c_int( 50 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_U_INTER_ACT_HORMONAL       = c_int( 51 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_HORMONAL  = c_int( 52 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BASE             = c_int( 53 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRUESA                     = c_int( 54 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTIG                   = c_int( 55 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BRUTO            = c_int( 61 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PACK                       = c_int( 62 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HORMA                      = c_int( 63 ).value

AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_NACIONALES                 = c_int(  1 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_PROVINCIAL                 = c_int(  2 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_MUNICIPAL                   = c_int(  3 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_INTERNOS                    = c_int(  4 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_INGRESOS_BRUTOS                      = c_int(  5 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA                    = c_int(  6 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS        = c_int(  7 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_POR_IMPUESTOS_MUNICIPALES = c_int(  8 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES                   = c_int(  9 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_OTROS                                = c_int( 99 ).value

AFIP_CODIGO_FORMA_DE_PAGO_CARTA_DE_CREDITO_DOCUMENTARIO       = c_int(  1 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CARTAS_DE_CREDITO_SIMPLE            = c_int(  2 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUE                              = c_int(  3 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUES_CANCELATORIOS               = c_int(  4 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CREDITO_DOCUMENTARIO                = c_int(  5 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CUENTA_CORRIENTE                    = c_int(  6 ).value
AFIP_CODIGO_FORMA_DE_PAGO_DEPOSITO                            = c_int(  7 ).value
AFIP_CODIGO_FORMA_DE_PAGO_EFECTIVO                            = c_int(  8 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ENDOSO_DE_CHEQUE                    = c_int(  9 ).value
AFIP_CODIGO_FORMA_DE_PAGO_FACTURA_DE_CREDITO                  = c_int( 10 ).value
AFIP_CODIGO_FORMA_DE_PAGO_GARANTIAS_BANCARIAS                 = c_int( 11 ).value
AFIP_CODIGO_FORMA_DE_PAGO_GIROS                               = c_int( 12 ).value
AFIP_CODIGO_FORMA_DE_PAGO_LETRAS_DE_CAMBIO                    = c_int( 13 ).value
AFIP_CODIGO_FORMA_DE_PAGO_MEDIOS_DE_PAGO_DE_COMERCIO_EXTERIOR = c_int( 14 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_DOCUMENTARIA          = c_int( 15 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_SIMPLE                = c_int( 16 ).value
AFIP_CODIGO_FORMA_DE_PAGO_PAGO_CONTRA_REEMBOLSO               = c_int( 17 ).value
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_DOCUMENTARIA                 = c_int( 18 ).value
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_SIMPLE                       = c_int( 19 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO                  = c_int( 20 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_DEBITO                   = c_int( 21 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TICKET                              = c_int( 22 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA              = c_int( 23 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_NO_BANCARIA           = c_int( 24 ).value
AFIP_CODIGO_FORMA_DE_PAGO_OTROS_MEDIOS_DE_PAGO                = c_int( 99 ).value





# -----------------------------------------------------------------------------
# Function: dll_version()
# -----------------------------------------------------------------------------
def dll_version():

  #title 
  print "*** DLL VERSION ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # get dll version
  str_version_max_len = 500
  str_version = create_string_buffer( b'\000' * str_version_max_len )
  int_major = c_int()
  int_minor = c_int()
  error = Handle_HL.ConsultarVersionDll( str_version, c_int(str_version_max_len).value, byref(int_major), byref(int_minor) )
  print "DllVersion            : ",
  print error
  print "String Dll Version    : ",
  print str_version.value
  print "Major Dll Version     : ",
  print int_major.value
  print "Minor Dll Version     : ",
  print int_minor.value


# -----------------------------------------------------------------------------
# Function: dll_version()
# -----------------------------------------------------------------------------
def dll_ll_test_comm():

  #title 
  print "*** DLL LOW LEVEL ***"
  print " "

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  print "OpenPort()"
  Handle_HL.setComPort(0)  # usb
  Handle_HL.setBaudRate( 115200 )
  Handle_HL.setProtocolType( c_int(1) )  # protocol extended
  Handle_HL.OpenPort()  # open 
  error = Handle_HL.getLastError()  
  print "OpenPort() Error : ",
  print error

  # getState
  print "getState()"
  error = Handle_HL.getState()
  print "getState() Error: ",
  print error
  

# -----------------------------------------------------------------------------
# Function: equipment_machine_version()
# -----------------------------------------------------------------------------
def equipment_machine_version():
  #title 
  print "*** EQUIPMENT MACHINE VERSION ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect                 : ",
  print error

  # get dll version
  str_version_max_len = 500
  str_version = create_string_buffer( b'\000' * str_version_max_len )
  int_major = c_int()
  int_minor = c_int()
  error = Handle_HL.ConsultarVersionEquipo( str_version, c_int(str_version_max_len).value, byref(int_major), byref(int_minor) )
  print "Machinne Version        : ",
  print error
  print "String Machinne Version : ",
  print str_version.value
  print "Major Machinne Version  : ",
  print int_major.value
  print "Minor Machine Version   : ",
  print int_minor.value
  
  # status
  error = Handle_HL.ConsultarEstadoDeConexion()
  print "Conexion Status         : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect               : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header_trailer()
# -----------------------------------------------------------------------------
def set_and_get_header_trailer():

  #title 
  print "*** HEADER & TRAILER ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error


  # set header #1
  error = Handle_HL.EstablecerEncabezado( c_int(1).value, "Nuevo Encabezado #1" )
  print "Config Header Error   : ",
  print error

  # get header #1
  str_header1_max_len = 100
  str_header1 = create_string_buffer( b'\000' * str_header1_max_len )
  error = Handle_HL.ConsultarEncabezado( c_int(1).value, str_header1, c_int(str_header1_max_len).value )
  print "Get Header Error      : ",
  print error
  print "Header #1 String      : ",
  print str_header1.value


  # set trailer #1
  error = Handle_HL.EstablecerCola( c_int(1).value, "Nueva Cola #1" )
  print "Config Trailer Error  : ",
  print error

  # get trailer #1
  str_trailer1_max_len = 100
  str_trailer1 = create_string_buffer( b'\000' * str_trailer1_max_len )
  error = Handle_HL.ConsultarCola( c_int(1).value, str_trailer1, c_int(str_trailer1_max_len).value )
  print "Get Trailer Error     : ",
  print error
  print "Trailer #1 String     : ",
  print str_trailer1.value


  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header()
# -----------------------------------------------------------------------------
def set_and_get_datetime():
  #title 
  print "*** DATE & TIME ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # get datetime
  str_datetime_max_len = 100
  str_datetime = create_string_buffer( b'\000' * str_datetime_max_len )
  error = Handle_HL.ConsultarFechaHora( str_datetime, c_int(str_datetime_max_len).value )
  print "Get Date & Time Error : ",
  print error
  print "Date & Time           : ",
  print str_datetime.value

  # set datetime (use the same value)
  error = Handle_HL.EstablecerFechaHora( str_datetime.value  )
  print "Set Date & Time Error : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header()
# -----------------------------------------------------------------------------
def cancel_all():

  #title 
  print "*** CANCEL ALL ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, c_int(str_doc_number_max_len).value )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, c_int(str_doc_type_max_len).value )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # get last error
  error = Handle_HL.ConsultarUltimoError()
  print "Last Error            : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: print_X_and_Z()
# -----------------------------------------------------------------------------
def print_X_and_Z():

  # get handle from DLL
  Handle_HL= ctypes.cdll.LoadLibrary("/home/facu-reyesoft/lib64/libEpsonFiscalInterface.so")
  # Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "serial:/dev/ttyUSB0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error
  
  # print X
  error = Handle_HL.ImprimirCierreX()
  print "Closure Cashier       : ",
  print error

  # print Z
  error = Handle_HL.ImprimirCierreZ()
  print "Closure Day           : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket
# -----------------------------------------------------------------------------
def ticket():

  #title 
  print "*** TICKET ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUET )
  print "Open                  : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, c_int(str_doc_number_max_len).value )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, c_int(str_doc_type_max_len).value )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error
  
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1.1234", "100.1234", ID_TASA_IVA_21_00, ID_IMPUESTO_INTERNO_FIJO, "7.1234", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.1", c_int(0).value, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.03", c_int(0).value, "CodigoInterno4567891123456789012345678901234567891"  )
  print "Uplift                : ",
  print error

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_from_ticket_invoice
# -----------------------------------------------------------------------------
def ticket_from_ticket_invoice():

  #title 
  print "*** TICKET FROM INVOICE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()

  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # open - without customer data previously loaded
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, c_int(str_doc_number_max_len).value )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, c_int(str_doc_type_max_len).value )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1", ".12", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # item 2
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Banana (item2)", "10", "132.087", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno5555588999922255999999600000000000001", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 2                : ",
  print error
  
  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value
  
  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.00", c_int(0).value, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.00", c_int(0).value, "CodigoInterno4567890122222222222225678901234567892"  )
  print "Uplift                : ",
  print error

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_invoice
# -----------------------------------------------------------------------------
def ticket_invoice():

  #title 
  print "*** TICKET INVOICE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_invoice_B
# -----------------------------------------------------------------------------
def ticket_invoice_B():

  #title 
  print "*** TICKET INVOICE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_debit_note
# -----------------------------------------------------------------------------
def ticket_debit_note():

  #title 
  print "*** TICKET DEBIT NOTE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error

# -----------------------------------------------------------------------------
# Function: ticket_debit_note_B
# -----------------------------------------------------------------------------
def ticket_debit_note_B():

  #title 
  print "*** TICKET DEBIT NOTE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_credit_note
# -----------------------------------------------------------------------------
def ticket_credit_note():

  #title 
  print "*** TICKET CREDIT NOTE ***"
  
  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "081-0005-0007777" )
  print "main source voucher   : ",
  print error
  
  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_credit_note_B
# -----------------------------------------------------------------------------
def ticket_credit_note_B():

  #title 
  print "*** TICKET CREDIT NOTE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "081-0005-0007777" )
  print "main source voucher   : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: download
# -----------------------------------------------------------------------------
def download():

  #title 
  print "*** DOWNLOAD CTD, CTD A and SUMMARY OF TOTALS ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel vouchers
  error = Handle_HL.Cancelar()
  print "Cancel voucher        : ",
  print error

  # download 
  error = Handle_HL.Descargar( "1", "1", "donwloads" )
  print "Download              : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: audit
# -----------------------------------------------------------------------------
def audit():

  #title 
  print "*** AUDIT ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( c_int(9600).value )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel voucher        : ",
  print error

  # audit 
  error = Handle_HL.ImprimirAuditoria( ID_MODIFICADOR_AUDITORIA_DETALLADA, "1", "2" )
  print "Audit Detailed        : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel Audit          : ",
  print error

  # audit 
  error = Handle_HL.ImprimirAuditoria( ID_MODIFICADOR_AUDITORIA_RESUMIDA, "1", "2" )
  print "Audit Summary         : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: send_fixed_invoice_body
# -----------------------------------------------------------------------------
def send_fixed_invoice_body( Handle_HL ):

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, c_int(str_doc_number_max_len).value )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, c_int(str_doc_type_max_len).value )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item  1  - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # load extra text descripcion  - annulation 
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4 (A): ",
  print error

  # item  1  - annulation
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_ANULAR, "Sardinas", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 1 - Annulation   : ",
  print error

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Rodondos (item2)"  )
  print "Extra Descript. #1    : ",
  print error

  # item  2
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Tomates (item2)", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno9999999999999999999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 2                : ",
  print error

  # item  3 - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION, "Cerveza (item3)", "2.0000", "3.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno8228888999922229999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_LITROS )
  print "Item 3 - new          : ",
  print error

  # item  3 - annulation
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION, "Cerveza (item3)", "2.0000", "3.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno8228888999922229999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_LITROS )
  print "Item 3 - Annulation   : ",
  print error

  # item  4 - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Banana (item4)", "1.0000", "2.3000", ID_TASA_IVA_10_50, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno5555588999922255999999600000000000001", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 4 - new          : ",
  print error

  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.00", c_int(0).value, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.00", c_int(0).value, "CodigoInterno4567222222222229012222222201234567890"  )
  print "Uplift                : ",
  print error

  # other taxes 1
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA, "Percepcion por Tasa de IVA", "10.00", ID_TASA_IVA_21_00 )
  print "VAT perception        : ",
  print error

  # other taxes 2
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES, "Otra Percepcion", "5.00", ID_TASA_IVA_NINGUNO )
  print "Other perception      : ",
  print error
  
  # other taxes 3
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS, "Percepcion de IIBB", "3.00", ID_TASA_IVA_NINGUNO )
  print "Other perception      : ",
  print error

  # payment 1  - new 
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO, c_int(3).value, "300.00", "Cupones", "Descripcion Pago #1", "VISA -4857, ctas. 3 x $100", "Descripcion Extra #2" )
  print "Payment 1 - new       : ",
  print error

  # payment 1  - annulation
  error = Handle_HL.CargarPago( ID_MODIFICADOR_ANULAR, AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO, c_int(3).value, "300.00", "Cupones", "Descripcion Pago #1", "VISA -4857, ctas. 3 x $100", "Descripcion Extra #2" )
  print "Payment 1 - annulation: ",
  print error

  # payment 2  - new
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA, c_int(0).value, "45.00", "Cupones", "Descripcion Pago ii", "CBU -878941494- Pago #2", "Descripcion Extra #2" )
  print "Payment 2 - new       : ",
  print error

  # payment 3  - new
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA, c_int(0).value, "25.00", "", "Descripcion Pago iii", "", "" )
  print "Payment 3 - new       : ",
  print error


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
print " "
print " "
print "----Basic Test"
# dll_version()
# dll_ll_test_comm()
# equipment_machine_version()
print_X_and_Z()
# set_and_get_header_trailer()
# set_and_get_datetime()
# cancel_all()
# print " "
# print " "
# print "----Testing Sales"
# ticket()
# ticket_from_ticket_invoice()
# ticket_invoice()
# ticket_invoice_B()
# ticket_debit_note()
# ticket_debit_note_B()
# ticket_credit_note()
# ticket_credit_note_B()
# print " "
# print " "
# print "----Test Close Day"
# audit()
# download()





