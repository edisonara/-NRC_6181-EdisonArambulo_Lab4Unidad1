#dibujar el uml......
# crear las clases atributos y metodos......
#  3. instanciar la superclase ......
# 4. instanciar la subclese ......
# lineas comentadas ........
#---------------------------------CLASE EMPLEADO -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------
class Empleado:
    def __init__ (self, nombre, edad, sueldo):
        ''' en vez de legado ponga expediente
                este es constructor;;;; 
                ;tiene una atributo y unoque es de tipo lista.''' 
        self.nombre = nombre
        self.edad = edad
        self.expediente = []              # expediente en lista 
        self.sueldoBase = sueldo
    def calcularSueldo(self, descuentos, bonos):
        ''' calcula el decuento
                retorna el sueldo total a pagar '''
        return float(self.sueldoBase - descuentos + bonos)


#----------------------------------CLASE EGENTE DE VENTA -------------------------------------------------
#---------------------------------------------------------------------------------------------------------
class AgenteVenta(Empleado):
    # reimplemetnacion de metodo __init__ en la subclase 
    def __init__(self, mostrador):
        """ este es constructor  con un solo parametro """
        self.numeroMostrador = mostrador


#---------------------------------------------- OPCION 1 -------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
def opc1():     # sin utilizar herencia
    '''funcion de la opcion 1 
        solo mandara datos del trabajador comun utilizando la superclase ->  class Empleado:
        '''
    trabajador  = Empleado('',0,0.0)             ## istancia de la superclase 
    listaExpediente=[]                           ### lista para el expediente 
    #----------------------------------------- INPUT OPCION 1 ------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    trabajador.nombre = input('ingrese nombre empleado: ')                             # ingresa nombre del empleado
    trabajador.edad = int(input('ingrese edad: '))                                     # ingresa edad del empleado 
    trabajador.sueldoBase = float(input('ingrese el sueldo base del empleado: '))      # ingresa sueldo del empleado
    print('\n INGRESE DATOS DEL EXPEDINTE:\n dato 1.- cargo que ocupa\n dato 2.- titulo profecional\n dato 3.-reconocimiento,\n dato 4.- discapacidad')                                            
    for a in range (1, 4, 1):                                                          # ingresa lista de expediente 4 opciones 
        dato = input(f'ingrese dato {a}:  ')
        listaExpediente.append(str(dato))
    for a in range(1,4, 1):
        trabajador.expediente = listaExpediente
                                                                                       # metodo CalcularSueldo................
                                                                                       # . a apartir de descuento y bono 
    descuento = float(input('ingrese el descuento aplicable: '))
    bono = float(input('ingrese el bono apicable: '))
    trabajador.calcularSueldo(descuento, bono)
    #------------------------------------OUPUT  OPCION 1-----------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    print(f'nombre del empleado es -> {trabajador.nombre}')
    print(f'edad del empleado es -> {trabajador.edad}')
    print(f'el sueldo es -> {trabajador.calcularSueldo(descuento, bono)}')              # metodo del sueldo total
    print (f'dato del expediente: {trabajador.expediente}')                             # el expediente en tipo lista


# ---------------------------------------- OPCION 2 ---------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
def opc2():  # utilizar herencia 
    '''funcion de la opcion 2 
        solo mandara datos del agente de ventas utilizando la subclase ->  class AgenteVenta(Empleado)
        '''
    edison = AgenteVenta(3)                  ### instancia de la subclase 
    listaExpediente=[]                       ### lista para el expediente 
    #---------------------------------------- INPUT OPCION 2 ------------------------------------------------------
    # --------------------------------------------------         --------------------------------------------------
    edison.nombre = input('ingrese nombre empleado: ')                         # ingresa nombre del empleado
    edison.edad = int(input('ingrese edad: '))                                 # ingresa edad del empleado 
    edison.sueldoBase = float(input('ingrese el sueldo base del empleado: '))    # ingresa sueldo del empleado
    print('\n INGRESE DATOS DEL EXPEDINTE:\n dato 1.- cargo que ocupa\n dato 2.- titulo profecional\n dato 3.-reconocimiento,\n dato 4.- discapacidad')                                            
    for a in range (1, 4, 1):                                                  # ingresa lista de expediente 4 opciones 
        dato = input(f'ingrese dato {a}:  ')
        listaExpediente.append(str(dato))
    for a in range(1,4, 1):
        edison.expediente = listaExpediente
    # metodo CalcularSueldo........................... a apartir de descuento y bono 
    descuento = float(input('ingrese el descuento aplicable: '))
    bono = float(input('ingrese el bono apicable: '))
    edison.calcularSueldo(descuento, bono)
    #-----------------------------------OUPUT OPCION 2-----------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------
    print(f'nombre del empleado es -> {edison.nombre}')
    print(f'edad del empleado es -> {edison.edad}')
    print(f'el sueldo es -> {edison.calcularSueldo(descuento, bono)}')          # metodo del sueldo total
    print(f' tiene el mostrador número :{ edison.numeroMostrador}')             # funcion de la subclase ->mostrador           
    print (f'dato del expediente: {edison.expediente}')                         # el expediente en tipo lista 

#--------------------------------- MENU PRINCIPAL  --------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
while True:
    '''es la parte principal del codigo 
        aqui se interactuan las funciones
        '''
    print('-------------menu------------------ ')
    print('op1. datos de empleado comun..')
    print('op2. datos del empleado agente de vetas. ')
    print('opc3. salir.')
    opcion = int(input('ingrese opción: '))
    if opcion == 1:
        opc1()                        # opcion con objeto de la superclase
    elif opcion == 2:
        opc2()                        # opcion del objeto de la subclase 
    elif opcion == 3:
        print('está saliendo mi pana ;) ')
        break                         # break para saltar de la repeticion del while 
    else:
        print('error de digito ')
