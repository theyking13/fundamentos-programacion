# edad=0
# entradas=0
# precio=0
# print("bienvenidos al parque nacional")

# print("cual es su edad:")

# edad=int(input("ingrese su edad:"))
# if edad<9:
#     print("es gratis")
# elif edad>=10:
#     print("paga $1000")
# elif edad>=18 and edad<=64:
#     print("paga $2000")
# elif edad>=65:
#     print("paga $15000")

# print("cuantas entradas desea")
# total_entradas=int(input("ingrese el total de entradas"))
# total_a_pagar=precio* total_entradas
# print(f"El total a pagar es:",total_a_pagar)
# ----------------ejercicio 2----------------------------

num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))

if num1 > num2 :
    print(f"el numero mayor es: {num1}")
elif num2 > num1 :
    print(f"el numero mayor es: {num2}")
else:
    print("ambos numero son iguales")



# ----------------ejercicio 3----------------------------

# for i in range(1, 11): 
#     for j in range(1, 11):  
#         print(f"{i} x {j} = {i * j}")
# print("-" * 15) 

# ----------------ejercicio 4 ----------------------------

# def mostrar_menu_principal():
#     print("\n--- Menú Principal ---")
#     print("1. Ingresar Nombre del Cliente")
#     print("2. Mostrar Menú de Platos con Precios")
#     print("3. Mostrar Saludo al Cliente")
#     print("4. Salir")
# def mostrar_menu_platos():
#     print("\n--- Menú de Platos ---")
#     print("1. Arroz a la francesa - $4.500")
#     print("2. Arroz marinero - $5.200")
#     print("3. Sopa marinera - $9.700")
#     print("-----------------------")
# def main():
#     nombre_cliente = "" 
#     while True:
#         mostrar_menu_principal()
#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             nombre_cliente = input("Ingrese el Nombre del Cliente: ").strip()
#             print(f"Nombre del cliente guardado: {nombre_cliente}")
#         elif opcion == "2":
#             mostrar_menu_platos()
#         elif opcion == "3":
#             if nombre_cliente:
#                 print(f"Gracias, {nombre_cliente}, por venir al restaurante Panuchis.")
#             else:
#                 print("Primero debe ingresar el nombre del cliente (opción 1).")
#         elif opcion == "4":
#             print("Saliendo del programa. ¡Hasta pronto!")
#             break
#         else:
#             print("Opción no válida. Por favor, intente nuevamente.")
# main()