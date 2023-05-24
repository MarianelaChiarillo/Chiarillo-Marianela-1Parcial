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
    8. Agregar Marca.
    9. Ingrese de que tipo de formato desea guardar el archivo (csv o json).
    10. Salir""")
    opcion = input("Ingrese una opción: ")
    return opcion