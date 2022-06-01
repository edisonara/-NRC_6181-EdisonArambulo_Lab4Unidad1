
import datetime
#### CLASE TIENDA 
class Tienda:
    def __init__(self, nomTienda,estadoTienda, gerente):
        self.atrib1 = nomTienda
        self.atrib2 = estadoTienda # @1
        self.atrib3 = gerente


    
## CLASE CLIENTE
class Cliente(Tienda):

    def __init__(self, nom, telef, estado):
        self.atributo1 = nom 
        self.atributo2 = int(telef)
        self.atributo3 = int(estado)
    
    def RegistCuenta(self):# @1
        self.atributo1= input('ingrese nombre: ')
        self.atributo2 = int(input('ingrese # telefono: '))
        self.usuario = self.atributo1 + '123'
        print(self.usuario)

    def IniciarSeccion(self): # @2
        self.usuarioRes = input('ingrese un usario para ingresar: ')
        while self.usuarioRes==self.usuario:
            print('un saludo para usted.....')
            break
                
    def RegistrarseTienda(self): # @3
        self.dia = datetime.date(2020,1,1)
        self.hora = datetime.time()
        self.entrarTienda = input('ingrese la tienda que desea ingresar:  ')
        self.dia = input('ingrese año, mes y dia: ')
        self.hora = input('ingrese hora y minutos: ')
        if self.entrarTienda == self.atrib1:
            print(f'registrado enla tienda {self.atrib1}, en la fecha [{self.dia}] y hora [{self.hora}] ')
        else:
            print('no se registro...')
            
    def HistoryTiendaVisita(self):# @4    Nro. Fecha Hora Tienda
        ## hacerlo con ficheros 
        pass

    def VerEstado(self): # @5
        print(f'nonbre: {self.atributo1}, numero de telefono: {self.atributo2}usted consta como estado: {self.atributo3}')

    def __str__(self):
        return(f'los datos son {self.atributo1}, {self.atributo2}, {self.atributo3}')




### CLASE ADMINISTRADOR 
class Admin(Cliente):
    def verDatosClientes(self,nom, tele, estado, gerente):   #  @1
        print(f'los datos son: nombre: {nom}, num telefono {tele}, estado{estado}')
        if gerente != '':
            print(f'y gerente {gerente}')

    def cambiarEstadoCliente(self): # @2
        self.estadoCliente = input(f'actualizar estado dela persona {self.atributo1}; si o no  ')
        if self.estadoCliente == 'si':
            if str(self.dia) == '2022:05:24':
                self.atributo3 = 3
        
    def cabiarEstadoTienda(self):
        self.estadoTienda = input(f'actualizar estado dela persona {self.atributo1}; si o no  ')
        if self.estadoTienda == 'si':
            if self.atributo3 == 3 :
                self.atrib2 = 2

### menu principal 
if __name__ == '__main__':
    usuario1= Cliente('',0,False)
    while True:
        #menu 1
        print('\n------- eliga opcion ----------')
        print('op 1: opciones del cliente')
        print('op 2: opciones del administrador.')
        print('op 3: salir.')
        opMenu = int(input('la opcion es? : '))
        ##menu 2
        if opMenu==1:
            while True:
                print('===========')
                print('......opciones del cliente......')
                print('op1: registro al sistema.')
                print('op2: inicie secion')
                print('opc3: menu principal\n')
                while True:
                    opCliente = int(input('ingrese la opcion.: '))
                    if opCliente <= 3:
                        break

                if opCliente==1:       ## parte uno del usuario 
                    usuario1.RegistCuenta()
                elif opCliente==2:
                     ## parte 2 del codigo 
                    ##### aqui se pressentara el reto del las obciones para el cliente
                    usuario1.IniciarSeccion()
                    while True:
                        opcion= int(input('ingrese opcion\n 1. registrarse en la tienda.\n 2. ver historial de visitas\n 3. ver estado.\n 4. salir.'))
                        if opcion == 1:
                            usuario1.RegistrarseTienda()
                        if opcion == 2:
                            usuario1.HistoryTiendaVisita()
                        if opcion ==3:
                            usuario1.VerEstado()
                        if opcion == 4:
                            print('salir... ')
                        if opcion== 4:
                            break

                else:     
                    print('saliendo al menu principal...')
                if opCliente == 3:
                    break

                
        elif opMenu==2:
            print('==========')
        elif opMenu==3:
            print('usted salio mi pana ;) ')
        else:
            print('error ;)')
        if opMenu ==3:
            break
        
