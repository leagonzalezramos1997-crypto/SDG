def valor_total(inventario):
    total = 0
    for producto in inventario:
        total += producto['precio'] * producto['cantidad']
    return total

def modificar_precio(inventario, nombre, nuevo_precio):
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['precio'] = nuevo_precio
            return True
    return False

def modificar_cantidad(inventario, nombre, nueva_cantidad):
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['cantidad'] = nueva_cantidad
            return True
    return False