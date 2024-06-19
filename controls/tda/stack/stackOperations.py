from CONTROLADOR.tda.linked.linkedList import Linked_List
from CONTROLADOR.exception.linkedEmpty import LinkedEmpty
class StackOperations(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        return self._lenght < self.__tope
    
    def push(self, data):
        if self.verifyTop:
            self.add(data, 0)
        else:
            print("Stack full")
            #raise LinkedEmpty("Stack full")
    
    @property
    def pop(self):
        if self.isEmpty:
            #raise LinkedEmpty("Stack empty")
            print("Stack full")
        else:
            
            data = self.get(0)
            self.delete(0) 
            return data 
    
#¿explicame el codigo de arriba?
#El código de arriba es un ejemplo de una pila, 
#que es una estructura de datos que sigue el principio de LIFO 
#(Last In First Out), es decir, el último elemento que entra es el 
#primero en salir. En este caso, la pila se implementa utilizando una 
#lista enlazada, que es una estructura de datos que consta de nodos que 
#contienen un valor y una referencia al siguiente nodo. La clase Stack 
#hereda de la clase Linked_List, que es una lista enlazada, y agrega un 
#método push que agrega un elemento a la pila. El método push agrega el 
#elemento al final de la lista enlazada y actualiza el tope de la pila 
#con el nuevo elemento. Además, la clase Stack tiene un método verifyYp 
#que verifica si la pila está dentro de su límite superior (tope). 
#En resumen, el código implementa una pila utilizando una lista enlazada 
#y proporciona métodos para agregar elementos a la pila y verificar 
#si la pila está dentro de su límite superior.
            
        