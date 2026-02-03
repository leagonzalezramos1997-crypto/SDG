import modulos.validaciones as validaciones
import modulos.gestion_datos as gestion

def crear_producto():
    while True:
        nombre = input("\nIngrese el nombre del producto: ")
        
        if not validaciones.validar_nombre(nombre):
            print("Error: El nombre no puede estar vacio")
            continue
        
        if validaciones.producto_existe(gestion.Inventario, nombre):
            print("Error: Este producto ya existe")
            continuar = input("Desea ingresar otro? (s/n): ")
            if continuar.lower() != 's':
                return None
            continue
        
        while True:
            precio = input("Ingrese el precio del producto: ")
            if validaciones.validar_precio(precio):
                precio_num = float(precio)
                break
            print("Error: El precio debe ser un numero positivo")
        
        while True:
            cantidad = input("Ingrese la cantidad del producto: ")
            if validaciones.validar_cantidad(cantidad):
                cantidad_num = int(cantidad)
                break
            print("Error: La cantidad debe ser un numero entero no negativo")
        
        return {
            "nombre": nombre,
            "precio": precio_num,
            "cantidad": cantidad_num
        }