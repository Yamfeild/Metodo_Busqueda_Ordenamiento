from flask import Blueprint, jsonify, abort, request, render_template, redirect
from controls.RegistroDaoControl import RegistroDaoControl
from datetime import datetime
from controls.dao.daoAdapter import DaoAdapter
from controls.tda.linked.ordenar.mergeSort import MergeSort
from controls.tda.linked.ordenar.quickSort import QuickSort
from controls.tda.linked.ordenar.shellSort import ShellSort
from controls.tda.linked.buscar.binary import Binary
from controls.tda.linked.buscar.lineal import Lineal
router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template("template.html")

@router.route('/registro')
def registros():
    rdc = RegistroDaoControl()
    lista = rdc._list() 
    
    
    return render_template("servp/registro.html", lista= rdc.to_dic_lista(lista))

@router.route('/ventanillas')
def ventanillas():
    return render_template("servp/ventanilla.html")

@router.route('/ventanillas/guardar', methods=['POST'])
def guardar_registro():
    rdc = RegistroDaoControl()
    data = request.form

    if not "nombre" in data.keys() or not "numVentanilla" in data.keys():
        abort(400)
    
    # Validar y guardar los datos
    rdc._ServidorPublico._numVentanilla = data['numVentanilla']
    rdc._ServidorPublico._nombre = data['nombre']
    rdc._ServidorPublico._fecha = data['fecha']
    rdc._ServidorPublico._calificacion = data['calificacion']
    rdc.save
    return redirect("/registro", code=302)

@router.route('/registro/modificar/<pos>')
def ver_editar(pos):
    fd = RegistroDaoControl()
    nene = fd._list().get(int(pos)-1)
    return render_template("servp/modificar.html", data=nene)

@router.route('/registro/modificar', methods=['POST'], )
def modificar_personas():
    fd = RegistroDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = fd._list().get(int(pos)-1)
    fd._ServidorPublico = nene
    fd._ServidorPublico._nombre = data['nombre']
    fd._ServidorPublico._fecha = data['fecha']
    fd._ServidorPublico._calificacion = data['calificacion']

    fd.merge(int(pos))
    return redirect("/registro", code=302)




@router.route('/registro/ordenar')
def orden_registros():

    rda = RegistroDaoControl()
    lista = rda._list()
    
    atributo = request.args.get('sort_by', '_apellido')
    metodo = request.args.get('metodo', 'quicksort')
    order = request.args.get('order', 'asc')
   
    tipo = 1 if order == 'asc' else 2

    lista.sort_models(atributo, tipo, metodo)

    return render_template('servp/registro.html', lista= rda.to_dic_lista(lista))

@router.route('/registro/buscar', methods=["GET"])
def buscar_datos():
    query = request.args.get("query")
    search_attribute = request.args.get("searchAttribute")
    search_method = request.args.get("metodo_busqueda")
    starts_with = request.args.get("startsWith") == "true"

    rda = RegistroDaoControl()
    lista = rda._list()
    array_personas = lista.toArray

    result = []
    if search_method == "binario":
        result = Binary.search(array_personas, search_attribute, query, starts_with)
        result = rda._list().toArray
    elif search_method == "lineal":
        result = Lineal.search(array_personas, search_attribute, query, starts_with)
    else:
        return "Método de búsqueda no válido"

    return render_template('servp/registro.html', lista=result)