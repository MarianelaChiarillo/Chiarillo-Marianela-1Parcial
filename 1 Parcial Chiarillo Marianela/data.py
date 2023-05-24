from menu import *
import csv
import re
import json
import os

def listar(lista: list[dict]): 
    lista = [] #lista vacia que va a pasar la funcion listar.

    with open('C:\\Users\\mari\\Desktop\\1 Parcial\\insumos.csv', 'r', encoding='utf-8') as file: #importo mi ruta donde esta ubicado el archivo csv.
        for linea in file:
            linea = linea.strip().split(",") #se lee cada linea del archivo y con el strip se eliminan los espacios y con el split se divide en una lista de elementos con coma.
            if len(linea) == 5:  # Verificar que la línea tenga 5 elementos.
                lista_dicts = { #cada palabra del encabezado cumple un lugar.
                    "ID": linea[0],
                    "NOMBRE": linea[1],
                    "MARCA": linea[2],
                    "PRECIO": linea[3],
                    "CARACTERISTICAS": linea[4]
                }
                lista.append(lista_dicts) # junto a la lista todos los datos.
    return lista

#--------------------------------------------------------------------------------------------------------------------------------

def marcar_cantidad(lista: list[dict]) -> set:

    marcas = set() #set marcas para almacenar las marcas sin duplicados.

    for diccionario in lista:
        marca = diccionario.get('MARCA') #cada dict, se consigue el valor  de la clave 'MARCA' utilizando  get(). 
        #Si se encuentra un valor válido  se agrega la marca al set.
        if marca:
            marcas.add(marca) #Si se encuentra un valor válido  se agrega la marca al set.

    print("""
---------------------------------- 
Cantidad de elementos por marca:
----------------------------------  
        """)
    for marca in marcas: #itera sobre cada marca en el conjunto marcas.
        cantidad = len(list(filter(lambda x: x.get('MARCA') == marca, lista)))#la función filter junto con una expresión lambda para filtrar los elementos .
        print(f"* {marca} = {cantidad}")

#--------------------------------------------------------------------------------------------------------------------------------

def listar_insumos_por_marca(lista: list[dict]):
    marcas = set()  # Conjunto para almacenar las marcas sin duplicados

    for diccionario in lista:
        marca = diccionario.get('MARCA')  # Obtener el valor del índice 'MARCA' del diccionario
        if marca:  # Verificar si se encontró una marca válida
            marcas.add(marca)  # Agregar la marca al conjunto

    print("""
---------------------------------- 
Listado de insumos por marca:
----------------------------------  
        """)

    for marca in marcas:
        print(f"Marca: {marca}")
        insumos_filtrados = filter(lambda x: x.get('MARCA') == marca, lista)  # Filtrar insumos por marca

        insumos_lista = []  # Lista para almacenar los insumos de la marca actual

        for insumo in insumos_filtrados:
            nombre = insumo.get('NOMBRE')  # Obtener el nombre del insumo
            precio = insumo.get('PRECIO')  # Obtener el precio del insumo

            insumos_lista.append(f"  Nombre: {nombre}, Precio: {precio}")

        print('\n'.join(insumos_lista))  # Imprimir la lista completa de insumos de la marca
        print("."*90)

#-------------------------------------------------------------------------------------------------------------------------

def buscar(lista: list[dict]):
    coincidencias = [] #Lista que va a recibir todas las coincidencias.

    for producto in lista: #itea en la lista de insumos.
        caracteristicas = producto["CARACTERISTICAS"] #se tiene el value de la clave lo que seria las caracteristicas.
        if re.match(rf'.*\b{clave.lower()}\b.*', caracteristicas.lower()): #el re match lo utilizo para buscar coincidencias por lo que se buscan coincidnecias en la palabra clave.
            coincidencias.append(producto) #cualquier caracteristica lo integro.

    if coincidencias: # si hay coincidencias imprimo toda la informacion.
        print("""
--------------------------------------------
 Coincidencias encontradas con su búsqueda:
--------------------------------------------""")
        
        for producto in coincidencias:
            marca = producto["MARCA"]
            caracteristicas = producto["CARACTERISTICAS"].split("~")
            for caracteristica in caracteristicas:
                print(f"Marca: {marca}")
                print(f"Característica: {caracteristica}")
                print("."*70)
    else:
        print("* Lo siento, no se han encontrado coincidencias.") #si no hay caracteristicas mando un mensaje.

#-----------------------------------------------------------------------------------------------------------------------

def ordenar_insumos(lista:list[dict])->list:
    insumos_ordenados = sorted(lista, key=lambda x: (x['MARCA'])) #utilizo el lambda para ejecutar la funcion sorted que me ordena por la marca.
    return insumos_ordenados #retorno esos insumos ordenados.


def listar_insumos_ordenados(lista:list)->list:
    insumos_ordenados = ordenar_insumos(lista) #Paso el resultado que obtuve al ordenarlo por marca.

    print("""
---------------------------------- 
Listado de insumos ordenados:
----------------------------------  
    """)

    for insumo in insumos_ordenados:
        caracteristicas = insumo['CARACTERISTICAS'].split("~")  # Separar las características.
        primera_caracteristica = caracteristicas[0] if caracteristicas else ""  # Obtengo una caracteristica o nada.

        print(f"ID: {insumo['ID']}, Nombre: {insumo['NOMBRE']}, Marca: {insumo['MARCA']}, Precio: {insumo['PRECIO']}, Características: {primera_caracteristica}")
        print("." * 70)

#-----------------------------------------------------------------------------------------------------------------------------

def mostrar_productos_por_marca(lista:list, marca:str)->list:
    productos = filter(lambda producto: producto['MARCA'].lower() == marca.lower(), lista) #utilizo filter para que me filtre todos los elementos por el valor marca, y lo condiciono con un lower.
    return list(productos) #retorno todos esos productos.

def realizar_compras(lista:list)->list:
    carrito_compras = [] #lista de compras vacia.
    total_compra = 0 #el contador de precio lo inicializo a 0.

    while True: #mientras sea verdad.
        marca = input("Ingrese la marca de los productos que desea comprar si desea finalizar o terminar escriba 'salir': ") #Pido que el usuario ingrese la marca.
        if marca.lower() == 'salir': #para terminar con todo el bucle.
            break

        productos = mostrar_productos_por_marca(lista, marca) #llamo a la funcion de mostrar productos.
        if not productos:
            print("Lo siento, no se encontraron productos de la marca seleccionada.") #si no se encuentra en la lista se muestra el mensaje.
            continue #si no continuo.

        print("Productos disponibles:") #muestro los productos que hay disponibles en esa marca y su precio.
        for producto in productos:
            print(f"{producto['NOMBRE']} - Precio: {producto['PRECIO']}")

        opcion_elegida = int(input("Ingrese el producto que desea (poner de forma numerica segun el orden de la lista): ")) # el usuario ingresa cual quiere.
        if opcion_elegida < 1 or opcion_elegida > len(productos): #se verifica que la opcion no se exceda los limites.
            print("Lo siento, su opcion no se encuentra.")
            continue #si no continuo

        producto_opcion_elegida = productos[opcion_elegida - 1] # se asigna el producto seleccionado de la lista segun su indice.
        cantidad = int(input("Ingrese la cantidad deseada: "))
        precio = (producto_opcion_elegida['PRECIO']).replace('$', '') #utilizo el replace asi la forma numerica se separa del signo.
        subtotal = float(precio)* cantidad #multiplico el precio por cantidad.
        total_compra += subtotal
        
        carrito_compras.append({ #appendeo al carrito de compras.
            'Producto': producto_opcion_elegida['NOMBRE'],
            'Precio': producto_opcion_elegida['PRECIO'],
            'Cantidad': cantidad,
            'Subtotal': subtotal
        })

    print(""" 
--------------------------
   Detalle de su compra:
--------------------------""") #lo muestro por pantalla.
    for item in carrito_compras:
        print(f"Producto: {item['Producto']}, Cantidad: {item['Cantidad']}, Subtotal: {item['Subtotal']}")

    print(f"*Total de la compra--> {total_compra}")

    generar_factura(carrito_compras, total_compra) #retorno el generar factura en base a la funcion de hacer un txt.

def generar_factura(carrito_compras:str, total_compra:float):
    with open('factura.txt', 'w') as file: #abro un file en formato txt.
        file.write("|Factura de su compra|\n")
        file.write("."*50 + "\n")
        for item in carrito_compras: #itero en los productos y muestro todos en la factura.
            file.write(f"--> Producto: {item['Producto']}\nCantidad: {item['Cantidad']}\nSubtotal: {item['Subtotal']}\n")
        file.write(f"*Total de su compra: {total_compra}\n")
    print("--> Se ha generado su facturación en un file de texto, gracias por su compra.")

#---------------------------------------------------------------------------------------------------------------------------

def guardar_json(rutaJSON: str, lista: list[dict]) -> None: #guardo como json para escritura.
    productos_filtrados = [producto for producto in lista if 'Alimento' in producto['NOMBRE']] #si esta producto con la palabra alimento en nombre los integro.

    with open(rutaJSON, 'w') as file:
        json.dump(productos_filtrados, file, indent=4) #guardo ese producto identado para que quede legible.

# rutaJSON = "insumos_alimento.json"  # Ruta donde se guardará el archivo JSON
# guardar_json(rutaJSON, lista)  # Llamada a la función para guardar los productos en formato JSON


def leer_json(ruta: str) -> list[dict]: #Para leer el json en la terminal hago esta funcion.
    with open(ruta, 'r') as file:
        diccionario = json.load(file)
    return diccionario

ruta_json = 'insumos_alimento.json'
lista_insumos = leer_json(ruta_json)

#-------------------------------------------------------------------------------------------------------------------------

def aplicar_aumento(producto: dict)-> float: #Aplico aumento al producto de la lista.
    precio_actual = producto['PRECIO'] #consigo el valor del precio.
    precio_dividido = precio_actual.split('$') # separo el numero del precio con el signo.
    if len(precio_dividido) > 1: #si hay signo en el precio separado se fija si es mayor que 1 y aplica aumento.
        numero_precio = float(precio_dividido[1]) #convierte los numeros de precio separado en float.
        precio_actualizado = numero_precio * 1.084 #aplico aumento.
        producto['PRECIO'] = f"${precio_actualizado:.2f}"
    return producto


# Obtener la lista de productos
ruta_csv = 'Insumos.csv' #defino ruta.
lista_productos = listar(ruta_csv) 

# Aplicar el aumento utilizando la función map
lista_productos_actualizados = list(map(aplicar_aumento, lista_productos)) #utilizo map para aplicar el aumento a los productos.

def guardar_csv(ruta: str, lista_productos: list):
    with open(ruta, 'w', newline='', encoding='utf-8') as file:
        # Escribir productos con precios actualizados
        for producto in lista_productos: #se itera sobre la lista de productos.
            linea = f"{producto['ID']},{producto['NOMBRE']},{producto['MARCA']},{producto['PRECIO']},{producto['CARACTERISTICAS']}\n"
            file.write(linea)


ruta_actualizada = 'Insumos_actualizados.csv' # Guardar los productos actualizados en el archivo "Insumos.csv"
# guardar_csv(ruta_actualizada, lista_productos_actualizados)


def leer_csv(ruta: str): #utilizo para leer el archivo con los precios actualizados.
    lista_retorno = [] #me retorna la lista con todos los productos.
    with open(ruta, 'r', newline='', encoding='utf-8') as file:
        for linea in file:
            linea = linea.strip()
            lista_aux = linea.split(',')
            lista_retorno.append(lista_aux) #a la lista retorno se le integra la lista auxiliar separada.
    return lista_retorno

#-----------------------------------------------------------------------------------------------------------------------------------

flag_bienvenida = False
while True:
    os.system("cls")

    match(menu()):
            case "s":
                print("Entendido, comencemos.")
                flag_bienvenida = True

            case "1":
                if flag_bienvenida:
                    lista = listar([])  # Pasa una lista vacía como argumento
                    marcar_cantidad(lista)
                        
                else:
                    print("Debe poner confirmar para saber más información.")

            case "2":
                if flag_bienvenida:
                    lista = listar([])  # Obtener la lista de insumos
                    listar_insumos_por_marca(lista)  # Mostrar los insumos por marca
                else:
                    print("Debe poner confirmar para saber más información.")

            case "3":
                if flag_bienvenida:
                    clave = input("Ingrese la característica que desea buscar --> ")
                    clave = clave.lower()
                    lista = listar([])
                    buscar(lista)

                else:
                    print("Debe poner confirmar para saber más información.")

            case "4":
                 if flag_bienvenida:
                    lista_insumos = listar([])  # Lista de insumos.
                    listar_insumos_ordenados(lista_insumos)
                    
                 else:
                     print("Debe poner confirmar para saber más información.")

            case "5":
                if flag_bienvenida:
                    lista = listar([])  
                    realizar_compras(lista)
                else:
                     print("Debe poner confirmar para saber más información.")

            case "6":
                if flag_bienvenida:
                    print(lista_insumos)
                else:
                    print("Debe poner confirmar para saber más información.")

            case "7":
                if flag_bienvenida:                   
                    ruta_actualizada = 'Insumos_actualizados.csv'
                    lista_retorno = leer_csv(ruta_actualizada)
                    print(lista_retorno)

            #         ruta_actualizada = 'Insumos_actualizados.csv'
            #         leer_csv(ruta_actualizada)
                else:
                    print("Debe poner confirmar para saber más información.")
        
            case "8":
                 salir = input("confirma salida? s/n: ")
                 if(salir == "s"):
                     break
    input("Presione enter para continuar")


