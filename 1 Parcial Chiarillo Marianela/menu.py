from data import *

def menu():

    print("""
    *** Menu de opciones ***"
    -----------------------
    Bienvenido, comenzamos? s/n
    1. Listar cantidad por marca.
    2. Listar insumos por marca.
    3. Buscar insumo por característica.
    4. Listar insumos ordenados.
    5. Realizar compras.
    6. Leer desde formato JSON.
    7. Actualizar precios.
    8. Salir""")
    opcion = input("Ingrese una opción: ")
    return opcion