from model.registroVentanilla import RegistroVentanilla
from controls.dao.daoAdapter import DaoAdapter
class RegistroDaoControl(DaoAdapter):
    def __init__(self):     
        super().__init__(RegistroVentanilla)
        self.__ServidorPublico = None
    
    @property
    def _ServidorPublico(self):
        if self.__ServidorPublico is None:
            self.__ServidorPublico = RegistroVentanilla()
        return self.__ServidorPublico

    @_ServidorPublico.setter
    def _ServidorPublico(self, value):
        self.__ServidorPublico = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._ServidorPublico._id = self._lista._length + 1
        self._save(self._ServidorPublico)
        
    
    def merge(self,pos):
        self._merge(self._ServidorPublico, pos)