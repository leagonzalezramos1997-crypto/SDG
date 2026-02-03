#IMPORTACIONES

import modulos.datos_basicos as datos
import modulos.gestion_datos as gestion
import modulos.funciones_utiles as utiles
import modulos.validaciones as validaciones

#Funciones del menú

def mostrar_menu():

    print("\n" + "="*30)
    print("   SISTEMA DE GESTIÓN")
    print("="*30)
    print("1. Agregar producto")
    print("2. Listado de productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Valor total del inventario")
    print("6. Modificar precio de producto")
    print("7. Modificar cantidad de producto")
    print("8. Salir \n ")

def bucle_menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
     
            if opcion == 1:
                print("\nCree producto en el sistema\n")
                producto = datos.crear_producto()
                gestion.agregar_producto(producto)     
           
            elif opcion == 2:
                print("\nMostrando inventario\n")
                gestion.mostrar_inventario()
     
            elif opcion == 3:
                print("\nBuscador de producto\n")
                nombre = input("Ingrese el nombre del producto a buscar: ")
                resultados = gestion.buscar_producto(nombre)
                if resultados:
                    print(f"\nResultados para '{nombre}'\n")
                    for producto in resultados:
                        print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
                else:
                    print(f"\nNo se encontró el producto '{nombre}'\n")
     
            elif opcion == 4:
                print("\nEliminando producto\n")
                gestion.eliminar_producto(input("Ingrese el nombre del producto a eliminar: "))

            elif opcion == 5:
                print("\nValor total del inventario\n")
                total = utiles.valor_total(gestion.Inventario)
                print(f"El valor total del inventario es: ${total:.2f}\n")

            elif opcion == 6:
                print("\nModificar precio de producto")
                nombre = input("Ingrese el nombre del producto: ")
                
                if not gestion.buscar_producto(nombre):
                    print(f"Error: Producto '{nombre}' no encontrado")
                    continue
                
                while True:
                    nuevo_precio = input("Ingrese el nuevo precio: ")
                    if validaciones.validar_precio(nuevo_precio):
                        if utiles.modificar_precio(gestion.Inventario, nombre, float(nuevo_precio)):
                            print("Precio modificado exitosamente")
                        break
                    print("Error: Precio invalido")

            elif opcion == 7:
                print("\nModificar cantidad de producto")
                nombre = input("Ingrese el nombre del producto: ")
                
                if not gestion.buscar_producto(nombre):
                    print(f"Error: Producto '{nombre}' no encontrado")
                    continue
                
                while True:
                    nueva_cantidad = input("Ingrese la nueva cantidad: ")
                    if validaciones.validar_cantidad(nueva_cantidad):
                        if utiles.modificar_cantidad(gestion.Inventario, nombre, int(nueva_cantidad)):
                            print("Cantidad modificada exitosamente")
                        break
                    print("Error: Cantidad invalida")
            
            elif opcion == 8:
                print("\nSaliendo del sistema\n")
                break
     
            else:
                print("\nOpción no válida. Por favor, intente de nuevo.\n")
       
        except ValueError:
            print("\nEntrada no válida. Por favor, ingrese un número.\n")