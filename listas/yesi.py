def inicializar_estacionamiento():
    filas = 6
    espacios_por_fila = 12
    return [['Disponible' for _ in range(espacios_por_fila)] for _ in range(filas)]

def ver_estado(estacionamiento):
    for i, fila in enumerate(estacionamiento):
        print(f"Fila {i+1}: {fila}")

def reservar_espacio(estacionamiento, ingresos_totales, fila, espacio):
    precios = [3000 if i < 2 else 1500 for i in range(6)]
    
    if estacionamiento[fila-1][espacio-1] == 'Disponible':
        estacionamiento[fila-1][espacio-1] = 'Reservado'
        ingresos_totales += precios[fila-1]
        print(f"Espacio {espacio} en fila {fila} reservado con éxito.")
    else:
        print(f"Espacio {espacio} en fila {fila} ya está reservado.")
    
    return ingresos_totales

def anular_reserva(estacionamiento, ingresos_totales, fila, espacio):
    precios = [3000 if i < 2 else 1500 for i in range(6)]
    
    if estacionamiento[fila-1][espacio-1] == 'Reservado':
        estacionamiento[fila-1][espacio-1] = 'Disponible'
        ingresos_totales -= precios[fila-1]
        print(f"Reserva del espacio {espacio} en fila {fila} anulada con éxito.")
    else:
        print(f"Espacio {espacio} en fila {fila} no está reservado.")
    
    return ingresos_totales

def totalizar_ingresos(ingresos_totales):
    print(f"Ingresos totales del día: {ingresos_totales} pesos.")

def menu():
    estacionamiento = inicializar_estacionamiento()
    ingresos_totales = 0

    while True:
        print("\nMenú de opciones:")
        print("1. Reservar estacionamiento.")
        print("2. Buscar estacionamiento.")
        print("3. Ver estado del estacionamiento.")
        print("4. Totalizar ventas del día.")
        print("5. Salir.")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            fila = int(input("Ingrese el número de fila (1-6): "))
            espacio = int(input("Ingrese el número de espacio (1-12): "))
            ingresos_totales = reservar_espacio(estacionamiento, ingresos_totales, fila, espacio)

        elif opcion == '2':
            fila = int(input("Ingrese el número de fila (1-6): "))
            espacio = int(input("Ingrese el número de espacio (1-12): "))
            
            if estacionamiento[fila-1][espacio-1] == 'Disponible':
                print(f"Espacio {espacio} en fila {fila} está disponible.")
            else:
                print(f"Espacio {espacio} en fila {fila} está reservado.")

        elif opcion == '3':
            ver_estado(estacionamiento)

        elif opcion == '4':
            totalizar_ingresos(ingresos_totales)

        elif opcion == '5':
            print("Saliendo del programa. ¡Que tenga un buen día!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def guardar_en_txt():
    codigo = """\
def inicializar_estacionamiento():
    filas = 6
    espacios_por_fila = 12
    return [['Disponible' for _ in range(espacios_por_fila)] for _ in range(filas)]

def ver_estado(estacionamiento):
    for i, fila in enumerate(estacionamiento):
        print(f"Fila {i+1}: {fila}")

def reservar_espacio(estacionamiento, ingresos_totales, fila, espacio):
    precios = [3000 if i < 2 else 1500 for i in range(6)]
    
    if estacionamiento[fila-1][espacio-1] == 'Disponible':
        estacionamiento[fila-1][espacio-1] = 'Reservado'
        ingresos_totales += precios[fila-1]
        print(f"Espacio {espacio} en fila {fila} reservado con éxito.")
    else:
        print(f"Espacio {espacio} en fila {fila} ya está reservado.")
    
    return ingresos_totales

def anular_reserva(estacionamiento, ingresos_totales, fila, espacio):
    precios = [3000 if i < 2 else 1500 for i in range(6)]
    
    if estacionamiento[fila-1][espacio-1] == 'Reservado':
        estacionamiento[fila-1][espacio-1] = 'Disponible'
        ingresos_totales -= precios[fila-1]
        print(f"Reserva del espacio {espacio} en fila {fila} anulada con éxito.")
    else:
        print(f"Espacio {espacio} en fila {fila} no está reservado.")
    
    return ingresos_totales

def totalizar_ingresos(ingresos_totales):
    print(f"Ingresos totales del día: {ingresos_totales} pesos.")

def menu():
    estacionamiento = inicializar_estacionamiento()
    ingresos_totales = 0

    while True:
        print("\\nMenú de opciones:")
        print("1. Reservar estacionamiento.")
        print("2. Buscar estacionamiento.")
        print("3. Ver estado del estacionamiento.")
        print("4. Totalizar ventas del día.")
        print("5. Salir.")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            fila = int(input("Ingrese el número de fila (1-6): "))
            espacio = int(input("Ingrese el número de espacio (1-12): "))
            ingresos_totales = reservar_espacio(estacionamiento, ingresos_totales, fila, espacio)

        elif opcion == '2':
            fila = int(input("Ingrese el número de fila (1-6): "))
            espacio = int(input("Ingrese el número de espacio (1-12): "))
            
            if estacionamiento[fila-1][espacio-1] == 'Disponible':
                print(f"Espacio {espacio} en fila {fila} está disponible.")
            else:
                print(f"Espacio {espacio} en fila {fila} está reservado.")

        elif opcion == '3':
            ver_estado(estacionamiento)

        elif opcion == '4':
            totalizar_ingresos(ingresos_totales)

        elif opcion == '5':
            print("Saliendo del programa. ¡Que tenga un buen día!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
"""
    
    with open("estacionamiento.txt", "w", encoding="utf-8") as archivo:
        archivo.write(codigo)
    print("Código guardado en 'estacionamiento.txt'.")

guardar_en_txt()
