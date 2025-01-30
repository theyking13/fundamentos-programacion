# hotel=[
#     [ 1, 2, 3, 4, 5, 6],
#     [ 7, 8, 9,10,11,12],
#     [13,14,15,16,17,18],
#     [19,20,21,22,23,24],
#     [25,26,27,28,29,30],
#     [31,32,33,34,35,36],
#     [37,38,39,40,41,42],
#     [43,44,45,46,47,48],    
#     [49,50,51,52,53,54]
#     [55,56,57,58,59,60]
# ]


# hotel = [["" for _ in range(6)] for _ in range (10)]
# def mostrar_estado():
#     print("\nEstado del hotel:")
#     for piso in range(10):
#         print(f"Piso {piso + 1}:", end="")
#         for habitacion in range(6):
#             if hotel[piso][habitacion] =="":
#                 print("[vacia]", end="")
#             else:
#                 print(f"[{hotel [piso] [habitacion]}]", end="")
#         print()
#     print()
    
# def agendar_habitacion():
#     try:
#         piso =int(input("ingrese el numero de piso (1-10):")) -1
#         habitacion = int(input("ingrese el numero de habitacion (1-6):")) -1
#         if 0 <= piso < 10 and 0 <= habitacion < 6:
#             if hotel[piso][habitacion] == "":
#                 nombre = input("ingrese el nombre del huesped:")
#                 hotel[piso][habitacion] = nombre
#                 print(f"habitacion {habitacion + 1} en piso {piso + 1} reservada para {nombre}.")
#             else:
#                 print("¡la habitacion ya esta ocupada!")
#         else:
#             print("numero de piso o habitacion invalidos.")
#     except ValueError:
#         print("Error: ingrese un numero valido.")
       
# def menu():
#     while True:
#         print("\nMenu del hotel")
#         print("1. Agendar habitacion")
#         print("2. Ver estado del hotel")
#         print("3. Salir")
#         opcion = input("Seleccione una opcion:")
        
#         if opcion == "1":
#             agendar_habitacion()
#         elif opcion == "2":
#             mostrar_estado()
#         elif opcion == "3":
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("opcion invalida. intente de nuevo.")
            
# menu()

# PRECIO_HABITACION = 78500
# IVA = 0.19
# hotel = [["" for _ in range(6)] for _ in range (10)]
# def mostrar_estado():
#     print("\nEstado del hotel:")
#     for piso in range(10):
#         print(f"Piso {piso + 1}:", end="")
#         for habitacion in range(6):
#             if hotel[piso][habitacion] =="":
#                 print("[vacia]", end="")
#             else:
#                 print(f"[{hotel [piso] [habitacion]}]", end="")
#         print()
#     print()
    
# def agendar_habitacion():
#     try:
#         piso =int(input("ingrese el numero de piso (1-10):")) -1
#         habitacion = int(input("ingrese el numero de habitacion (1-6):")) -1
#         if 0 <= piso < 10 and 0 <= habitacion < 6:
#             if hotel[piso][habitacion] == "":
#                 nombre = input("ingrese el nombre del huesped:")
#                 hotel[piso][habitacion] = nombre
#                 print(f"habitacion {habitacion + 1} en piso {piso + 1} reservada para {nombre}.")
#             else:
#                 print("¡la habitacion ya esta ocupada!")
#         else:
#             print("numero de piso o habitacion invalidos.")
#     except ValueError:
#         print("Error: ingrese un numero valido.")

# def vaciar_habitacion():
#     try:
#         piso =int(input("ingrese el numero de piso (1-10):")) -1
#         habitacion = int(input("ingrese el numero de habitacion (1-6):")) -1
#         if 0 <= piso < 10 and 0 <= habitacion < 6:
#             if hotel[piso][habitacion] == "":
#                 print(f"habitacion {habitacion + 1} en piso {piso + 1} liberada.")
#                 hotel[piso][habitacion] = ""
#             else:
#                 print("¡la habitacion ya esta vacia!")
#         else:
#             print("numero de piso o habitacion invalidos.")
#     except ValueError:
#         print("Error: ingrese un numero valido.")

# def calculadora_ingresos():
#     total_habitaciones = sum(1 for piso in hotel for hab in piso if hab !="")
#     subtotal = total_habitaciones * PRECIO_HABITACION
#     total_con_iva = subtotal * (1 + IVA)
    
#     print("\nResumen de ingresos:")
#     print(f"Habitaciones ocupadas: {total_habitaciones}")
#     print(f"Subtotal: ${subtotal:, .0f}")
#     print(f"total con iva ({IVA*100}%): ${total_con_iva:, .0f}\n")
               
# def menu():
#     while True:
#         print("\nMenu del hotel")
#         print("1. Agendar habitacion")
#         print("2. Ver estado del hotel")
#         print("3. Vaciar habitacion")
#         print("4. Ver ingresos")
#         print("3. Salir")
#         opcion = input("Seleccione una opcion:")
        
#         if opcion == "1":
#             agendar_habitacion()
#         elif opcion == "2":
#             mostrar_estado()
#         elif opcion == "3":
#             vaciar_habitacion()
#         elif opcion == "4":
#             calculadora_ingresos()
#         elif opcion == "5":
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("opcion invalida. intente de nuevo.")
            
# menu()

import os

PRECIO_HABITACION = 78500
IVA = 0.19
ARCHIVO_HOTEL="hotel_data.txt"
hotel = [["" for _ in range(6)] for _ in range (10)]
def cargar_datos():
    if os.path.exists(ARCHIVO_HOTEL):
        with open(ARCHIVO_HOTEL, "r") as file:
            datos = [line.strip().split(",") for line in file.readlines()]
            return[[hab if hab != "vacia" else "" for hab in piso] for piso in datos]
        return [["" for _ in range(6)] for _ in range (10)]
def guardar_datos():
    with open (ARCHIVO_HOTEL, "w") as file:
        for piso in hotel:
            file.write(",".join(hab if hab else "vacia" for hab in piso) + "\n")
           
def mostrar_estado():
    print("\nEstado del hotel:")
    for piso in range(10):
        print(f"Piso {piso + 1}:", end="")
        for habitacion in range(6):
            if hotel[piso][habitacion] =="":
                print("[vacia]", end="")
            else:
                print(f"[{hotel [piso] [habitacion]}]", end="")
        print()
    print()
    
def agendar_habitacion():
    try:
        piso =int(input("ingrese el numero de piso (1-10):")) -1
        habitacion = int(input("ingrese el numero de habitacion (1-6):")) -1
        if 0 <= piso < 10 and 0 <= habitacion < 6:
            if hotel[piso][habitacion] == "":
                nombre = input("ingrese el nombre del huesped:")
                hotel[piso][habitacion] = nombre
                print(f"habitacion {habitacion + 1} en piso {piso + 1} reservada para {nombre}.")
            else:
                print("¡la habitacion ya esta ocupada!")
        else:
            print("numero de piso o habitacion invalidos.")
    except ValueError:
        print("Error: ingrese un numero valido.")

def vaciar_habitacion():
    try:
        piso =int(input("ingrese el numero de piso (1-10):")) -1
        habitacion = int(input("ingrese el numero de habitacion (1-6):")) -1
        if 0 <= piso < 10 and 0 <= habitacion < 6:
            if hotel[piso][habitacion] == "":
                print(f"habitacion {habitacion + 1} en piso {piso + 1} liberada.")
                hotel[piso][habitacion] = ""
            else:
                print("¡la habitacion ya esta vacia!")
        else:
            print("numero de piso o habitacion invalidos.")
    except ValueError:
        print("Error: ingrese un numero valido.")

def calculadora_ingresos():
    total_habitaciones = sum(1 for piso in hotel for hab in piso if hab !="")
    subtotal = total_habitaciones * PRECIO_HABITACION
    total_con_iva = subtotal * (1 + IVA)
    
    print("\nResumen de ingresos:")
    print(f"Habitaciones ocupadas: {total_habitaciones}")
    print(f"Subtotal: ${subtotal:, .0f}")
    print(f"total con iva ({IVA*100}%): ${total_con_iva:, .0f}\n")
               
def menu():
    while True:
        print("\nMenu del hotel")
        print("1. Agendar habitacion")
        print("2. Ver estado del hotel")
        print("3. Vaciar habitacion")
        print("4. Ver ingresos")
        print("3. Salir")
        opcion = input("Seleccione una opcion:")
        
        if opcion == "1":
            agendar_habitacion()
        elif opcion == "2":
            mostrar_estado()
        elif opcion == "3":
            vaciar_habitacion()
        elif opcion == "4":
            calculadora_ingresos()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("opcion invalida. intente de nuevo.")

hotel = cargar_datos()   
menu()