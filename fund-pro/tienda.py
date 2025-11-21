"""
Crea un programa que muestre un menú para un restaurante con 10 productos. 
El programa debe capturar cada venta en una lista y al final mostrar las ventas por tipo de producto y el total de las ventas.
Utiliza algunas funciones para capturar la información y listas para guardar los datos
"""

menu = [
    {"nombre": "Hamburguesa", "precio": 150},
    {"nombre": "Pizza", "precio": 200},
    {"nombre": "Ensalada", "precio": 90},
    {"nombre": "Sopa", "precio": 60},
    {"nombre": "Pasta", "precio": 120},
    {"nombre": "Pollo frito", "precio": 180},
    {"nombre": "Tacos", "precio": 100},
    {"nombre": "Sándwich", "precio": 80},
    {"nombre": "Batido", "precio": 40},
    {"nombre": "Pastel", "precio": 70}
]

# Lista global para almacenar todas las ventas :\
ventas = []

def mostrar_resumen_ventas():
    """Muestra el resumen final de todas las ventas"""
    print("\n" + "="*50)
    print("           RESUMEN DE VENTAS")
    print("="*50)
    
    total_general = 0
    ventas_por_producto = [0] * len(menu)
    
    # Calcular ventas por producto B)
    for venta in ventas:
        indice_producto, cantidad = venta
        ventas_por_producto[indice_producto] += cantidad
    
    # Mostrar resultados :P
    for i, total_vendido in enumerate(ventas_por_producto):
        if total_vendido > 0:
            producto = menu[i]
            subtotal = total_vendido * producto['precio']
            total_general += subtotal
            print(f"• {producto['nombre']:15} | {total_vendido:2} unidades | ${subtotal:5}")
    
    print("-"*50)
    print(f"TOTAL GENERAL: ${total_general}")
    print("="*50)

def capturar_venta():
    """Captura una venta individual"""
    while True:
        try:
            opcion = int(input("\nSelecciona el número del producto: "))
            if 1 <= opcion <= len(menu):
                cantidad = int(input("Ingresa la cantidad: "))
                if cantidad > 0:
                    return opcion - 1, cantidad
                else:
                    print("La cantidad debe ser mayor a 0")
            else:
                print("Opción no válida. Por favor selecciona un número del 1 al 10")
        except ValueError:
            print("Por favor, ingresa números válidos")


def mostrar_menu():
    """Muestra el menú de productos disponibles"""
    print("\n" + "="*40)
    print("          MENÚ DEL RESTAURANTE")
    print("="*40)
    for i, producto in enumerate(menu, 1):
        print(f"{i:2d}. {producto['nombre']:15} ${producto['precio']:5}")
    print("="*40)

def procesar_opcion(opcion):
    """Procesa la opción seleccionada por el usuario"""
    if opcion == 1:
        mostrar_menu()
    elif opcion == 2:
        mostrar_menu()
        venta_capturada = capturar_venta()
        if venta_capturada:
            indice, cantidad = venta_capturada
            producto = menu[indice]
            ventas.append((indice, cantidad))
            print(f" {cantidad} {producto['nombre']}(s) agregado(s) a la venta")
    elif opcion == 3:
        if ventas:
            mostrar_resumen_ventas()
        else:
            print("\nNo se registraron ventas hoy.")
        return True  
    return False  
def Mostrar_opciones():
    """Muestra las opciones principales y maneja la selección"""
    while True:
        try:
            print("\n" + "="*30)
            print("     SISTEMA DE VENTAS")
            print("="*30)
            print("[1] Mostrar menú")
            print("[2] Realizar venta")
            print("[3] Terminar y ver resumen")
            print("="*30)
            
            response = int(input("Selecciona una opción (1-3): "))
            if response in (1, 2, 3):
                return response
            print("Opción no válida. Intenta de nuevo")
        except ValueError:
            print("Por favor, ingresa un número válido")

def main():
    """Función principal del programa"""
    
    continuar = True
    while continuar:
        opcion = Mostrar_opciones()
        terminar = procesar_opcion(opcion)
        if terminar:
            continuar = False

# Ejecutar el programa
if __name__ == "__main__":
    main()