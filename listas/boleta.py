def guardar_boleta(productos, subtotal, iva, total, metodo_pago, comision):
    with open("boleta.txt", "w", encoding="utf-8") as file:
        file.write("----- BOLETA -----\n")
        file.write("Producto(s):\n")
        for producto in productos:
            file.write(f"- {producto}\n")
        file.write(f"\nSubtotal (sin IVA): ${subtotal:.2f}\n")
        file.write(f"IVA (19%): ${iva:.2f}\n")
        file.write(f"Comisión por pago ({metodo_pago}): ${comision:.2f}\n")
        file.write(f"TOTAL: ${total:.2f}\n")
        file.write("-------------------\n")
    print("\nLa boleta ha sido guardada en 'boleta.txt'.")

def mostrar_boleta(productos, subtotal, iva, total, metodo_pago, comision):
    print("\n----- BOLETA -----")
    print("Producto(s):")
    for producto in productos:
        print(f"- {producto}")
    print(f"\nSubtotal (sin IVA): ${subtotal:.2f}")
    print(f"IVA (19%): ${iva:.2f}")
    print(f"Comisión por pago ({metodo_pago}): ${comision:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print("-------------------")

    guardar_boleta(productos, subtotal, iva, total, metodo_pago, comision)

def calcular_total_recursivo(precios, indice=0):
    if indice == len(precios):
        return 0
    return precios[indice] + calcular_total_recursivo(precios, indice + 1)

def sistema_de_ventas():
    productos_disponibles = [
        ("entradas", 9000),
        ("cerveza", 5000),
        ("wisky", 25000),
        ("gin", 21000)
    ]

    print("Sistema de Ventas")
    print("-----------------")
    print("Productos disponibles:")
    for i, (nombre, precio) in enumerate(productos_disponibles, 1):
        print(f"{i}. {nombre} - ${precio}")

    productos_seleccionados = []
    precios_seleccionados = []

    while True:
        try:
            opcion = int(input("Ingrese el número del producto (0 para finalizar): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(productos_disponibles):
                producto, precio = productos_disponibles[opcion - 1]
                productos_seleccionados.append(producto)
                precios_seleccionados.append(precio)
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    if not productos_seleccionados:
        print("No se seleccionaron productos.")
        return

    subtotal = calcular_total_recursivo(precios_seleccionados)

    iva = subtotal * 0.19

    print("\nMétodos de pago:")
    print("1. Efectivo (0% comisión)")
    print("2. Débito (1.5% comisión)")
    print("3. Crédito (2.89% comisión)")

    while True:
        try:
            metodo = int(input("Seleccione el método de pago: "))
            if metodo == 1:
                comision = 0
                metodo_pago = "Efectivo"
                break
            elif metodo == 2:
                comision = (subtotal + iva) * 0.015
                metodo_pago = "Débito"
                break
            elif metodo == 3:
                comision = (subtotal + iva) * 0.0289
                metodo_pago = "Crédito"
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    total = subtotal + iva + comision

    mostrar_boleta(productos_seleccionados, subtotal, iva, total, metodo_pago, comision)

sistema_de_ventas()