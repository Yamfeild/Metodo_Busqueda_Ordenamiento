class RegistroVentanilla:
    def __init__(self):
        self.__id = 0
        self.__numVentanilla = 0
        self.__nombre = ""
        self.__calificacion = ""
        self.__fecha = ""
    

   

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value


    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _numVentanilla(self):
        return self.__numVentanilla


    @_numVentanilla.setter
    def _numVentanilla(self, value):
        self.__numVentanilla = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "numVentanilla": self.__numVentanilla,
            "nombre": self.__nombre,
            "calificacion": self.__calificacion,
            "fecha": self.__fecha,
            
        }
        
    def deserializar(data): 
        registroV = RegistroVentanilla()
        registroV._id = data["id"]
        registroV._numVentanilla = data["numVentanilla"]
        registroV._nombre = data["nombre"]
        registroV._calificacion = data["calificacion"]
        registroV._fecha = data["fecha"]
        
        return registroV