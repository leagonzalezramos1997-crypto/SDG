def validar_nombre(nombre):
    if not nombre or nombre.strip() == "":
        return False
    return True

def validar_precio(precio):
    try:
        precio_num = float(precio)
        return precio_num > 0
    except ValueError:
        return False

def validar_cantidad(cantidad):
    try:
        cantidad_num = int(cantidad)
        return cantidad_num >= 0
    except ValueError:
        return False

def producto_existe(inventario, nombre):
    for producto in inventario:
        if producto['nombre'].lower() == nombre.lower():
            return True
    return False
