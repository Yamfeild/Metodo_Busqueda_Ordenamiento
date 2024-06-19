from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException 
from controls.tda.linked.ordenar.mergeSort import MergeSort
from controls.tda.linked.ordenar.quickSort import QuickSort
from controls.tda.linked.ordenar.shellSort import ShellSort
from controls.tdaArray import TDAArray
from numbers import Number

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node.data = data
            
    
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    
    def delete(self, pos = 0):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    

    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)


    
    #Pasar la lista a arreglo
    @property
    def toArray(self):
        array = TDAArray(self._length)
        if not self.isEmpty:
            node = self.__head
            cont = 0 
            while cont < self._length:
                array.insert(node._data, cont)
                cont += 1
                node = node._next
        return array
    
    def search_equals(self,data):
        list = Linked_List
        if self.isEmpty:
            raise LinkedEmpty("List Empty")
        else:
            array = self.toArray
            #print(len(array))
            for i in range(0, len(array)):
                #print(array[i])
                if(array[i].lower().endswith()):#constains= para buscar palabra en la mitad
                 list.add(array[i],list._length)
        return list
    

    def toList(self, array):
        self.clear
        for i in range (0 , len(array)):
            #self.__addLast__(array.get(i))
            self.__addLast__(array[i])

    def sort(self, type):
        array = self.toArray
        array = self.sort_burbuja_int(type, array)
        self.toList(array)

    def sort_burbuja_int(self, type, array):
        for i in range(0, len(array) -1):
            for j in range(0,len(array)-1):
                if type == 1:
                 if array[j-1]> array[j]:
                    temp = array [j-1]
                    array[j-1]= array[j]
                    array[j]= temp
                else:
                    array[j-1]< array[j]
                    temp = array [j-1]
                    array[j-1]= array[j]
                    array[j]= temp

        return array
    
    def sort(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], Number):
                array = self.sort_burbuja_number(1,array)
                self.toList(array)
                
    def sort_models(self, attribute, tipo=1, metodo=""):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if metodo == "quicksort":
                sorter = QuickSort()
            elif metodo == "mergesort":
                sorter = MergeSort()
            elif metodo == "shellsort":
                sorter = ShellSort()
            else:
                raise ValueError("Método de ordenación no soportado")

            if tipo == 1:
                array = sorter.sort_models_ascendent(array, attribute)
            else:
                array = sorter.sort_models_descendent(array, attribute)

            self.toList(array)
        return self
    


    def sort_cons(self, attribute, tipo=1, metodo=""):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if metodo == "quicksort":
                sorter = QuickSort()
            elif metodo == "mergesort":
                sorter = MergeSort()
            elif metodo == "shellsort":
                sorter = ShellSort()
            else:
                raise ValueError("Método de ordenación no soportado")

            if tipo == 1:
                array = sorter.sort_models_ascendent(array, attribute)
            else:
                array = sorter.sort_models_descendent(array, attribute)

            self.toList(array)
        return self