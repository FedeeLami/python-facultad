"""
Creación de un programa básico de gestión de inventario.
Desarrollar un programa en Python que permita gestionar un inventario
simple de productos, incluyendo funciones básicas como agregar productos,
eliminar productos y mostrar el inventario.
El programa debe tener un menú interactivo que permita al usuario
seleccionar las siguientes operaciones:
Agregar un nuevo producto al inventario, solicitando al usuario el nombre y
la cantidad inicial del producto.
Eliminar un producto existente del inventario, solicitando al usuario el
nombre del producto a eliminar.
Mostrar el inventario actual, que incluya el nombre y la cantidad de cada
producto.
Salir del programa.
El inventario puede ser almacenado utilizando un diccionario simple, donde
las claves sean los nombres de los productos y los valores sean las cantidades. Se
deben manejar situaciones simples como la introducción de productos duplicados
o la eliminación de productos inexistentes.
"""
def options():
    while True:
        print('1. Agregar producto')
        print('2. Eliminar producto')
        print('3. Mostrar inventario')
        print('4. Salir del programa')

        opcion = input('Ingrese un número para seleccionar: ')

        if opcion.isdigit() and (1 <= int(opcion) <= 4):
            return int(opcion)
        else:
            print('Respuesta no válida, ingrese un número entre 1 y 4')


inventario = []

while True:
    
    opcion = options()

    if opcion == 1:
        nombre = input('Ingrese nombre del producto para agregar: ').lower()
        
        while True:
            cantidad = input('Ingrese la cantidad de ese producto: ')
            if cantidad.isdigit():
                cantidad = int(cantidad)
                break
            else:
                print('Respuesta no válida, ingrese cantidad en números')

        existe = False
        for item in inventario:
            if nombre == item['producto']:
                item['cantidad'] += cantidad
                existe = True
                break       

        if not existe:
            inventario.append({
                "producto": nombre,
                "cantidad": cantidad
            })
 
    elif opcion == 2:
        nombre = input('Ingrese nombre del producto para eliminar: ').lower()
        existe = False

        for item in inventario:
            if item['producto'] == nombre:
                inventario.remove(item)
                existe = True
                break
            
        if not existe:
            print('El elemento no está en la lista')

    elif opcion == 3:
        if not inventario:
            print('El inventario está vacío')
        else:
            for item in inventario:
                print(f'Producto: {item["producto"]}, Cantidad: {item["cantidad"]}')
    
    elif opcion == 4:
        break 
