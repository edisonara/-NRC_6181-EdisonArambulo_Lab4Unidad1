import datetime
import requests
import os
import argparse
import re
import json

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR
from holidays.constants import JAN, MAY, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase

##=======================================    CLASE 1 =================================================================
# ========================================================================================================
# =
class FiestasEcuador(HolidayBase): # 
    """
   Clase para hacer mas sencillo los feriados.
        el cual tendra referncia las provincias las cuales son pasados por herencia.
                     https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (clase padre) 
    ---------- prov: str código de provincia según ISO3166-2 Métodos ------- 
        __init__(self, plate, date, time, online=False) : 
                 Construye todos los atributos necesarios para el objeto HolidayEcuador.
        _populate(self, year): Devuelve si una fecha es festiva o no
        """     
    # Códigos ISO 3166-2 (estan en los metodos)), 
    # # llamadas provincias
    # https://es.wikipedia.org/wiki/ISO_3166-2:EC
    IMPR_PROVINCIAS = ["EC-P"]  # TODO añadir más provincias

    def __init__(self, **kwargs):# kwargs a diferencia del self es un argumeto para poder declarar una funcion 
        """
             Construye todos los atributos necesarios para el objeto HolidayEcuador.
        """         
        self.country = "ECU"
        self.provincia = kwargs.pop("prov", "ON") # eliminar la clave especificada y devolver el valor correspondiente
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Comprueba si una fecha es festiva o no Parámetros 
        ----------
             año : str año de una fecha Devuelve 
         ------
             Devuelve verdadero si una fecha es festiva de lo contrario flase
        """                    
        # año nuevo 
        self[datetime.date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        
        # navidad
        self[datetime.date(year, DEC, 25)] = "Navidad [Christmas]"
        
        # semana Santa
        self[easter(year) + rd(weekday=FR(-1))] = "Semana Santa (Viernes Santo) [Good Friday)]"
        self[easter(year)] = "Día de Pascuas [Easter Day]"
        
        # Carnebaal
        total_lent_days = 46
        self[easter(year) - datetime.timedelta(days=total_lent_days+2)] = "Lunes de carnaval [Carnival of Monday)]"
        self[easter(year) - datetime.timedelta(days=total_lent_days+1)] = "Martes de carnaval [Tuesday of Carnival)]"
        
        # Día laboral
        name = "Día Nacional del Trabajo [Labour Day]"
        # # .- (Ley 858/Ley Reformatoria a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O 
        # #.-  906)) Si el feriado cae en sábado o martes 
        # # .-el descanso obligatorio irá al viernes o lunes inmediato anterior 
        # # .-respectivamente
        if year > 2015 and datetime.date(year, MAY, 1).weekday() in (5,1): # weekday, regresa el numero de la semana
            self[datetime.date(year, MAY, 1) - datetime.timedelta(days=1)] = name
        # (Ley 858/Ley Reformatoria a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) 
                # si el feriado cae en domingo 
        # # el descanso obligatorio irá al lunes siguiente
        elif year > 2015 and datetime.date(year, MAY, 1).weekday() == 6:# weekday, regresa el numero de la semana 
            self[datetime.date(year, MAY, 1) + datetime.timedelta(days=1)] = name # datetime.timedelta se usa para calcular las diferencias en las fechas
       # (Ley 858/Ley de Reforma a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) 
                # Los feriados que sean en miércoles o jueves 
       # # se trasladarán al viernes de esa semana
        elif year > 2015 and  datetime.date(year, MAY, 1).weekday() in (2,3):
            self[datetime.date(year, MAY, 1) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, MAY, 1)] = name
        
        #Batalla de Pichincha, las reglas son las mismas que el día del trabajo
        name = "Batalla del Pichincha [Pichincha Battle]"
        if year > 2015 and datetime.date(year, MAY, 24).weekday() in (5,1):
            self[datetime.date(year, MAY, 24).weekday() - datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, MAY, 24).weekday() == 6:
            self[datetime.date(year, MAY, 24) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, MAY, 24).weekday() in (2,3):
            self[datetime.date(year, MAY, 24) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, MAY, 24)] = name        
        
        # Primer Grito de Independencia, las reglas son las mismas que el día del trabajo
        name = "Primer Grito de la Independencia [First Cry of Independence]"
        if year > 2015 and datetime.date(year, AUG, 10).weekday() in (5,1):
            self[datetime.date(year, AUG, 10)- datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, AUG, 10).weekday() == 6:
            self[datetime.date(year, AUG, 10) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, AUG, 10).weekday() in (2,3):
            self[datetime.date(year, AUG, 10) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, AUG, 10)] = name       
        
        # Independencia de Guayaquil, las reglas son las mismas que el día del trabajo
        name = "Independencia de Guayaquil [Guayaquil's Independence]"
        if year > 2015 and datetime.date(year, OCT, 9).weekday() in (5,1):
            self[datetime.date(year, OCT, 9) - datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, OCT, 9).weekday() == 6:
            self[datetime.date(year, OCT, 9) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, MAY, 1).weekday() in (2,3):
            self[datetime.date(year, OCT, 9) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, OCT, 9)] = name        
        
        # Día de Muertos y
        namedd = "Día de los difuntos [Day of the Dead]" 
        # Independence of Cuenca
        nameic = "Independencia de Cuenca [Independence of Cuenca]"
        #(Ley 858/Ley Reformatoria a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) 
        # Para feriados nacionales y/o locales que coincidan en días corridos, 
        # se aplicarán las siguientes reglas:
        if (datetime.date(year, NOV, 2).weekday() == 5 and  datetime.date(year, NOV, 3).weekday() == 6):
            self[datetime.date(year, NOV, 2) - datetime.timedelta(days=1)] = namedd
            self[datetime.date(year, NOV, 3) + datetime.timedelta(days=1)] = nameic     
        elif (datetime.date(year, NOV, 3).weekday() == 2):
            self[datetime.date(year, NOV, 2)] = namedd
            self[datetime.date(year, NOV, 3) - datetime.timedelta(days=2)] = nameic
        elif (datetime.date(year, NOV, 3).weekday() == 3):
            self[datetime.date(year, NOV, 3)] = nameic
            self[datetime.date(year, NOV, 2) + datetime.timedelta(days=2)] = namedd
        elif (datetime.date(year, NOV, 3).weekday() == 5):
            self[datetime.date(year, NOV, 2)] =  namedd
            self[datetime.date(year, NOV, 3) - datetime.timedelta(days=2)] = nameic
        elif (datetime.date(year, NOV, 3).weekday() == 0):
            self[datetime.date(year, NOV, 3)] = nameic
            self[datetime.date(year, NOV, 2) + datetime.timedelta(days=2)] = namedd
        else:
            self[datetime.date(year, NOV, 2)] = namedd
            self[datetime.date(year, NOV, 3)] = nameic  
            
        # Fundación de Quito, aplica solo para la provincia de Pichincha, 
        # las reglas son las mismas que el día del trabajo
        name = "Fundación de Quito [Foundation of Quito]"        
        if self.provincia in ("EC-P"):
            if year > 2015 and datetime.date(year, DEC, 6).weekday() in (5,1):
                self[datetime.date(year, DEC, 6) - datetime.timedelta(days=1)] = name
            elif year > 2015 and datetime.date(year, DEC, 6).weekday() == 6:
                self[(datetime.date(year, DEC, 6).weekday()) + datetime.timedelta(days=1)] =name
            elif year > 2015 and  datetime.date(year, DEC, 6).weekday() in (2,3):
                self[datetime.date(year, DEC, 6) + rd(weekday=FR)] = name
            else:
                self[datetime.date(year, DEC, 6)] = name
#====================================   CLASE 2 ===========================================================
#===============================================================================================
class PicoPlaca:
    """
    Una clase para representar una medida de restricción vehicular (Pico y Placa) 
            - ORDENANZA METROPOLITANA No. 0305
    http://www7.quito.gob.ec/mdmq_ordenanzas/Ordenanzas/ORDENANZAS%20A%C3%91OS%20ANTERIORES/ORDM-305-%20%20CIRCULACION%20VEHICULAR%20PICO%20Y%20PLACA.pdf
    ...
    Atributos
    ----------
    placa : calle
        El registro o patente de un vehículo es una combinación de caracteres alfabéticos o numéricos
        caracteres que identifican e individualizan el vehículo respecto de los demás;
        
        El formato utilizado es
        XX-YYYY o XXX-YYYY,
        donde X es una letra mayúscula e Y es un dígito.
    fecha: calle
        Fecha en la que el vehículo pretende transitar
        esta siguiendo el
        Formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.
    tiempo: calle
        tiempo en que el vehículo pretende transitar
        esta siguiendo el formato
        HH:MM: por ejemplo, 08:35, 19:30
    en línea: booleano, opcional
        si en línea == Verdadero, se utilizará la API de días festivos abstractos
    Métodos
    -------
    __init__(self, plate, date, time, online=False):
        Construye todos los atributos necesarios.
        para el objeto PicoPlaca.
    plato (uno mismo):
        Obtiene el valor del atributo de placa
    placa (auto, valor):
        Establece el valor del atributo de la placa
    fecha (uno mismo):
        Obtiene el valor del atributo de fecha
    fecha (auto, valor):
        Establece el valor del atributo de fecha
    tiempo (uno mismo):
        Obtiene el valor del atributo de tiempo
    tiempo (uno mismo, valor):
        Establece el valor del atributo de tiempo
    __find_day(yo, fecha):
        Devuelve el día a partir de la fecha: 
        por ejemplo, miércoles
    __is_forbidden_time(self, check_time):
        Devuelve True si el tiempo proporcionado está dentro de las horas pico prohibidas,
         de lo contrario, Falso
    __es_vacaciones:
        Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
         de lo contrario, Falso
    predecir (auto):
        Devuelve True si el vehículo con la placa especificada puede estar en la carretera en la fecha y hora especificadas, 
        de lo contrario, 
        Falso    
        
        """ 
    #Days of the week
    __days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

    # Dictionary that holds the restrictions inf the form {day: forbidden last digit}
    __restrictions = {
            "Monday": [1, 2],
            "Tuesday": [3, 4],
            "Wednesday": [5, 6],
            "Thursday": [7, 8],
            "Friday": [9, 0],
            "Saturday": [],
            "Sunday": []}

    def __init__(self, placa, date, time, online=False):
        """
        Construye todos los atributos necesarios para el objeto PicoPlaca.
        
         Parámetros
         ----------
             placa : calle
                 El registro o patente de un vehículo es una combinación de caracteres alfabéticos o numéricos
                 caracteres que identifican e individualizan el vehículo respecto de los demás;
                 El formato utilizado es AA-YYYY o XXX-YYYY, donde X es una letra mayúscula e Y es un dígito.
             fecha: calle
                 Fecha en la que el vehículo pretende transitar
                 Sigue el formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22.
             tiempo: calle
                 tiempo en que el vehículo pretende transitar
                 Sigue el formato HH:MM: por ejemplo, 08:35, 19:30
             en línea: booleano, opcional
                 si en línea == Verdadero, se usará la API de días festivos abstractos (el valor predeterminado es Falso)               
        """                
        self.plate = placa
        self.date = date
        self.time = time
        self.online = online


    @property
    def plate(self):
        """
            Obtiene el valor del atributo de placa
        """
        return self._plate


    @plate.setter
    def plate(self, value):
        """
        Establece el valor del atributo de la placa
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato
             XX-YYYY o XXX-YYYY,
             donde X es una letra mayúscula e Y es un dígito
        """
        if not re.match('^[A-Z]{2,3}-[0-9]{4}$', value):
            raise ValueError(
                'La placa debe tener el siguiente formato: XX-YYYY o XXX-YYYY, donde X es una letra mayúscula e Y es un dígito')
        self._plate = value

        ###=========================================================================================================================================================================================================================================================
    @property
    def date(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._date


    @date.setter
    def date(self, value):
        """
        Establece el valor del atributo de fecha
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._date = value
        

    @property
    def time(self):
        """
            Obtiene el valor del atributo de tiempo
        """
        return self._time


    @time.setter
    def time(self, value):
        """
        Establece el valor del atributo de tiempo
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato HH:MM (por ejemplo, 08:31, 14:22, 00:01)
        """
        if not re.match('^([01][0-9]|2[0-3]):([0-5][0-9]|)$', value):
            raise ValueError(
                'La hora debe tener el siguiente formato: HH:MM (por ejemplo, 08:31, 14:22, 00:01)')
        self._time = value


    def __find_day(self, date):
        """
        Encuentra el día a partir de la fecha: por ejemplo, miércoles
         Parámetros
         ----------
         fecha: calle
             Está siguiendo el formato ISO 8601 AAAA-MM-DD: por ejemplo, 2020-04-22
         Devoluciones
         -------
         Devuelve el día a partir de la fecha como una cadena
        """        
        d = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        return self.__days[d]


    def __is_forbidden_time(self, check_time):
        """
        Comprueba si el tiempo proporcionado está dentro de las horas pico prohibidas,
         donde las horas pico son: 
         07:00 - 09:30 y 16:00 - 19:30
         Parámetros
         ----------
         check_time : str
             Tiempo que se comprobará. Está en formato HH:MM: 
             por ejemplo, 08:35, 19:15
         Devoluciones
         -------
         Devuelve True si el tiempo proporcionado está dentro de las horas pico prohibidas,
          de lo contrario, Falso
        """           
        t = datetime.datetime.strptime(check_time, '%H:%M').time()
        return ((t >= datetime.time(7, 0) and t <= datetime.time(9, 30)) or
                (t >= datetime.time(16, 0) and t <= datetime.time(19, 30)))


    def __is_holiday(self, date, online):
        """
        Comprueba si la fecha (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador
         si en línea == Verdadero, utilizará una API REST, 
         de lo contrario, generará los días festivos del año examinado
        
         Parámetros
         ----------
         fecha: calle
             Está siguiendo el formato ISO 8601 AAAA-MM-DD: 
             por ejemplo, 2020-04-22
         en línea: booleano, opcional
             si en línea == Verdadero, se utilizará la API de días festivos abstractos
         Devoluciones
         -------
         Devuelve True si la fecha marcada (en formato ISO 8601 AAAA-MM-DD) es un día festivo en Ecuador,
          de lo contrario, Falso        
          """            
        y, m, d = date.split('-')

        if online:
            # API de vacaciones abstractapi, versión gratuita: 1000 solicitudes por mes
             # 1 solicitud por segundo
             # recuperar la clave API de la variable de entorno
            key = os.environ.get('HOLIDAYS_API_KEY')
            response = requests.get(
                "https://holidays.abstractapi.com/v1/?api_key={}&country=EC&year={}&month={}&day={}".format(key, y, m, d))
            if (response.status_code == 401):
                # Esto significa que falta una clave API
                raise requests.HTTPError(
                    'Falta la clave API. Guarde su clave en la variable de entorno HOLIDAYS API_KEY')
            if response.content == b'[]':  # si no hay vacaciones, obtenemos una matriz vacía
                return False
            # Arreglar el Jueves Santo incorrectamente denotado como feriado
            if json.loads(response.text[1:-1])['name'] == 'Jueves Santo':
                return False
            return True
        else:
            ecu_holidays = FiestasEcuador(prov='EC-P')
            return date in ecu_holidays


    def predict(self):
        """
        Comprueba si el vehículo con la placa especificada puede estar en la carretera 
            en la fecha y hora proporcionada según las reglas de Pico y Placa:
        http://www7.quito.gob.ec/mdmq_ordenanzas/Ordenanzas/ORDENANZAS%20A%C3%91OS%20ANTERIORES/ORDM-305-%20%20CIRCULACION%20VEHICULAR%20PICO%20Y%20PLACA.pdf    
        Devoluciones
         -------
         Devoluciones
         Verdadero si el vehículo con
         la placa especificada puede estar en el camino
         en la fecha y hora especificadas, de lo contrario Falso
        """
        # Comprobar si la fecha es un día festivo
        if self.__is_holiday(self.date, self.online):
            return True

        # Verifique para vehículos excluidos de la restricción 
            # de acuerdo con la segunda letra de la placa o si usa solo dos letras

        # https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Ecuador
        if self.plate[1] in 'AUZEXM' or len(self.plate.split('-')[0]) == 2:
            return True

        # Compruebe si el tiempo proporcionado no está en las horas pico prohibidas
        if not self.__is_forbidden_time(self.time):
            return True

        day = self.__find_day(self.date)  # Compruebe si el tiempo proporcionado no está en las horas pico prohibidas
            #Buscar el día de la semana a partir de la fecha
         # Verifique si el último dígito de la placa no está restringido en este día en particular
        if int(self.plate[-1]) not in self.__restrictions[day]:
            return True

        return False

# ================================== FUNCION PRINCIPAL =====================================================
#===========================================================================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=
        'Predictor Pico y Placa Quito: Verifique si el vehículo con la placa proporcionada puede estar en la carretera en la fecha y hora proporcionada:')
    online = False

    '''EJEMPLO DE INGRESO EN CONSOLA:
            PARA LA PLACA: EBA-0234
            PARA LA FECHA: 2021-04-23
            PARA LA HORA: 15:15
    '''

    placa =input('ingrse placa:the vehicle\'s plate: XXX-YYYY or XX-YYYY, where X is a capital letter and Y is a digit.')
    fecha= input('ingrese, the date to be checked: YYYY-MM-DD:')
    time= input('ingrrse, the time to be checked: HH:MM:  ')
   

    pyp = PicoPlaca(placa,fecha , time, online)

    if pyp.predict():
        print(
            'El vehículo con placa {} PUEDE estar en la carretera el {} a las {}.'.format(
                placa,
                fecha ,
                time))
    else:
        print(
            'El vehículo con placa {} NO PUEDE estar en la carretera en {} a las {}.'.format(
                placa,
                fecha ,
                time))