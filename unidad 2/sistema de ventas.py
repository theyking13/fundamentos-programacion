def mostrar_boleta(productos, subtotal, iva, total, metodo_pago, comision):
    print("\n-----boleta-----")
    print("productos(s):")
    for producto in productos:
        print(f"-{producto}")
    print(f"\nsubtotal (sin iva): ${subtotal: .2f}")
    print(f"IVA (19%): ${iva: .2f}")
    print(f"comision por pago ({metodo_pago}): ${comision: .2f} ")
    print(f"total: ${total: .2f}")
    print("--------------------------")

def calculadora_total_recursivo(precios, indice=0):
    if indice == len(precios):
        return 0
    return precios [indice]  + calculadora_total_recursivo(precios, indice+1)

def sistema_de_ventas():
    productos_disponibles = [("carne 1", 15000),
                             ("bebidas 2", 2500),
                             ("libro 3", 20000),
                             ("entrada de futbol 4", 9000)]
    print("sistema_de_ventas")
    print("-----------------")
    print("productos disponibles: ")
    for i, (nombre, precio) in enumerate (productos_disponibles, 1):
        print(f"{i}. {nombre} - $ {precio}")
        productos_seleccionados = []
        precios_seleccionados = []

        while True:
            try:
                opcion =int(input("ingrese el numero del producto (0 para finalizar):" ))
                if opcion == 0:
                    break
                elif 1 <= opcion <= len(productos_disponibles):
                    producto, precio = productos_disponibles [opcion - 1]
                    productos_seleccionados.append(producto)
                    precios_seleccionados.append(precio)
                else:
                    print("opcion invalida intente nuevamente.")
            except ValueError:
                print("entrada no valida. intente nuevamente.")
        if not productos_seleccionados:
            print("no se seleccionaron productos.")
            return
        subtotal = calculadora_total_recursivo(precios_seleccionados)
        iva = subtotal * 0.19
        
        print("\nMetodos de pago:")
        print("1. Efectivo (0% comision)")
        print("2. debito (1.5% comision)")
        print("3.credito (2.89% comision)")

        while True:
            try:
                metodo = int(input("seleccione el metodo de pago:"))
                if metodo == 1:
                    comision = 0
                    metodo_pago = "efectivo"

                    break
                elif metodo == 2:
                    comision = 0.015
                    metodo_pago = "debito"

                    break
                elif metodo == 3:
                    comision = 0.0289
                    metodo_pago = "credito"

                    break
                else:
                    print("opcion invalida. intente nuevamente.")
            except ValueError:
                print("entrada no valida intente nuevamente")

                total = subtotal + iva + comision
            
            mostrar_boleta(productos_seleccionados, subtotal, iva, total, metodo_pago, comision)

sistema_de_ventas()