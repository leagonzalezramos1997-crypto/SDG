Inventario=[]
def agregar_producto(producto):
    Inventario.append(producto)
    return 

def eliminar_producto(nombre):
    for i, producto in enumerate(Inventario):
        if producto['nombre'] == nombre:
            return Inventario.pop(i)
    return None

def mostrar_inventario():

    #inventario en formato tabla
    
    print("\n" + "="*50)
    print("INVENTARIO ACTUAL")
    print("="*50)
    
    if len(Inventario) == 0:
        print("El inventario está vacío")
        return
    
    print(f"{'ID':<3} {'Nombre':<20} {'Precio':<10} {'Cantidad':<10}")
    print("-"*50)
    
    for i, producto in enumerate(Inventario, 1):
        print(f"{i:<3} {producto['nombre']:<20} ${producto['precio']:<9.2f} {producto['cantidad']:<10}")
    
    print("="*50)
    print(f"Total productos: {len(Inventario)}")

def buscar_producto(nombre):
    resultados = []
    for producto in Inventario:
        if producto['nombre']==nombre:
            resultados.append(producto)
    return resultados