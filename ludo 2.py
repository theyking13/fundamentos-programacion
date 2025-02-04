# import random

# def jugar_ludo():
#     print("bienvenido a jugar ludo.")
#     print("el objetivo es llegar a 24. si te pasas, pierdes.")
#     print("buena suerte.")
    
#     posicion=0
#     turno=1
     
#     while posicion < 24 :
#         input(f"\nturno {turno} : presiona enter para lanzar dado...")
#         dado = random.randint (1,6)
#         print("has sacado un {dado}.")
#         if posicion + dado >24 :
#             print(f"¡te pasaste! estas en posicion {posicion} y ahora tienes {posicion + dado}.")
#             print("¡has perdido el juego!")
#             return
#         posicion += dado 
#         print(f"tu nueva posicion es {posicion}.")
#         if posicion == 24:
#             print("¡felicidades! has llegado exactamente a 24. ¡ganaste el juego tomate un shot")
#             return
#         turno +=1

# jugar_ludo( )

# import random

# jugador1 = 0
# jugador2 = 0

# def rullete():
#     return random.randint(1,6)

# print("bienvenido a la ruleta rusa.")
# bala = rullete()
# for p in range(6):
#     print("turno del jugador" , p+1 )
#     print("para disparar precione enter")
#     mov=input()
#     if mov == "enter":
#         time.sleep(1)
#         print("*")
#         time.sleep(1)
#         print("*")
#         time.sleep(1)
#         print("*")
#         if p == bala:
#             print("bamg!!!")
#             break
#         else:
#             print("zafaste wey")


# import random

# hp_jugador1 = 60
# hP_jugador2= 60

# def daño():
#     return random.randint(2,10)

# print("bienvenido al street fighter de phyton")
# golpe = daño()
# turno=1
# while hp_jugador1 > 0 and hP_jugador2:
#     print(f"\nturno {turno}")
#     print(f"jugador 1 hp {hp_jugador1} 
#           jugador 2 hp: {hP_jugador2} ")
#     if random.random < 0.2:
#         daño=int(daño * 1.6)
#         print("jugador1 hace un daño critico   ")
    
     
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


def calcular_total_recursivo(precios, indice=0):
    if indice == len(precios):
        return 0
    return precios[indice] + calcular_total_recursivo(precios, indice + 1)


def sistema_de_ventas():
    # Lista de productos y precios
    productos_disponibles = [
        ("Producto 1", 1000),
        ("Producto 2", 2000),
        ("Producto 3", 3000),
        ("Producto 4", 4000)
    ]

    print("Sistema de Ventas")
    print("-----------------")
    print("Productos disponibles:")
    for i, (nombre, precio) in enumerate(productos_disponibles, 1):
        print(f"{i}. {nombre} - ${precio}")

    # Selección de productos
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

    # Calcular subtotal
    subtotal = calcular_total_recursivo(precios_seleccionados)

    # Calcular IVA
    iva = subtotal * 0.19

    # Selección del método de pago
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
                comision = subtotal * 0.015
                metodo_pago = "Débito"
                break
            elif metodo == 3:
                comision = subtotal * 0.0289
                metodo_pago = "Crédito"
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    # Calcular total
    total = subtotal + iva + comision

    # Mostrar boleta
    mostrar_boleta(productos_seleccionados, subtotal, iva, total, metodo_pago, comision)


# Ejecutar el sistema de ventas
sistema_de_ventas()
