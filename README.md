# SDG
Sistema de gestión de productos en python

### Características
- Validación de datos de entrada
- Manejo de errores básico
- Formato tabular para mostrar inventario
- Persistencia en memoria durante la ejecución
- Búsqueda por nombre exacto

## Estructura de Datos

Cada producto se almacena como un diccionario con:
- `nombre` (string): Nombre del producto
- `precio` (float): Precio unitario
- `cantidad` (int): Stock disponible

El inventario se almacena como una lista de diccionarios.

## Validaciones Implementadas

- Nombre no vacío
- Precio positivo
- Cantidad no negativa
- Evitar productos duplicados
- Entradas numéricas válidas
