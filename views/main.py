import sys


sys.path.append('../')
from controls.tda.linked.ordenar.quickSort import QuickSort
from controls.tda.linked.linkedList import Linked_List
from controls.RegistroDaoControl import RegistroDaoControl

import random
import time

rdc = RegistroDaoControl()
try:
    lista = Linked_List()
    for i in range(10000):
        lista.add(round(random.random()*10000))
    
    

    print("Tiempo de quicksort")
    inicio = time.time()
    lista.sort_models_ascendent()
    fin = time.time()
    print("Tiempo de ejecución: "+str(fin-inicio))

#    print("Tiempo de quicksort")    
#    inicio = time.time()
#    lista.sort(type=2, algorithm="quicksort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de mergesort") 
#    inicio = time.time()
#    lista.sort(type=1, algorithm="mergesort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de mergesort") 
#    inicio = time.time()
#    lista.sort(type=2, algorithm="mergesort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de shellsort") 
#    inicio = time.time()
#    lista.sort(type=1, algorithm="shellsort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de shellsort") 
#    inicio = time.time()
#    lista.sort(type=2, algorithm="shellsort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))

except Exception as error:
    print("Errores")
    print(error)