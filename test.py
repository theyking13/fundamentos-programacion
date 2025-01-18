# nombre="reinaldo hormazabal"
# edad="22"

# print("Mi nombre es",nombre, "Mi edad es", edad)
# num1=0
# num2=0

# print("ingrese un numero")
# num1=int(input())
# print("ingrese un numero")
# num2=int(input())

# print(num1+num2)

# print("ingrese un numero")
# num1=int(input())
# if num1>0:
#     print("el numero ingresado es positivo")
# else:
#     print("el numero es negativo o cero")

# print("ingrese un numero")
# num1=int(input())

# if num1>18:
#     print("es mayor de edad")
# else:
#     print("no es mayor de edad")

# num1=0
# num2=0
# num3=0

# print("ingrese el primer numero")
# num1=int(input())

# print("ingrese el segundo numero")
# num2=int(input())

# print("ingrese el tercer numero")
# num3=int(input())
# print((num1+num2+num3)/3)

# parque nacional que tiene los sigientes valores

# menor de 12$500
# entre 12 y 18 $1000
# entre 19 y 64 $2000
# mas de 65 $700

# bonus pregunte cuantas entradas son 

# edad=0
# entradas=0

# print("bienvenidos al parque nacional")

# print("cual es su edad")

# edad=int(input("ingrese su edad"))
# if edad<12:
#     print("paga $500")
# elif edad>=13 and edad<=18:
#     print("paga $1000")
# elif edad>=19 and edad<=64:
#     print("paga $2000")
# elif edad>=65:
#     print("paga $700")

# # entradas=0

# print("cuantas entradas desea")
# print("ingrese el total de entradas")
# total_entradas=int(input("ingrese el total de entradas"))
# print(f"el total de entradas es ")

# edad = int(input("¿Cuál es su edad? "))  


# if edad < 12:
#     precio = 500
#     print("Paga $500")
# elif edad >= 13 and edad <= 18:
#     precio = 1000
#     print("Paga $1000")
# elif edad >= 19 and edad <= 64:
#     precio = 2000
#     print("Paga $2000")
# elif edad >= 65:
#     precio = 700
#     print("Paga $700")


# print("¿Cuántas entradas desea?")
# total_entradas = int(input("Ingrese el total de entradas: "))


# total_a_pagar = precio * total_entradas
# print("El total a pagar es:",total_a_pagar)


# op1="si"
# op2="no"
# numero=0
# descuento=0

# num=7
# for i in range (22):
#     print("usted tiene", i+1, "años")
    
# for i in range(1, 11): 
#     for j in range(1, 11):  
#         print(f"{i} x {j} = {i * j}")
#     print("-" * 15) 
# total=0
# for i in range(2):
#     print("ingrese gasto")
#     gasto=int(input())
#     total=total+gasto
# print(total)

# for i in range (3):
#     print(, i+1, "años")
# promedio=0
# for i in range(3):
#     print("ingrese notas")
#     notas=int(input())
#     promedio=promedio+notas
# print("su promedio es" ,promedio/(i+1))

# for i in range(3):
#     num=0
#     if num%3==0:
#         print("el numero es par")
#     else:
#         print("el numero no es par")

# inicio = int(input("Ingrese el número inicial del rango: "))
# fin = int(input("Ingrese el número final del rango: "))

# print("Números impares en el rango:")
# for numero in range(inicio, fin + 1):
#     if numero % 2 != 0:
#         print(numero) 

# pal="reinaldo"
# print(len(pal))
# for i in pal:
#     print(i)

# total=0
# nom=input()
# for i in range(len(nom)):
#     total=total(i+1)
# print("el total")



# password_correcta="1234"

# for intento in range(1, 4):
#     password_ingresada= input("ingrese contraseña:")
#     if password_ingresada == password_correcta:
#         if intento == 1:
#             print("bienvenido al sistema")
#         else:
#             print("Contraseña correcta. Acceso concedido.")
#         break  
#     else:
#         print("Contraseña incorrecta. Intenta de nuevo.")
# else:
#     print("Has agotado los 3 intentos. Acceso denegado.")

# for i in range(10):
#     cont=int(input("ingrese su numero"))
#     if cont == num:
#         print("su numero es correcto el numero es:" ; num)
#         break
#     if cont<num:
#         print("el numero es mayor, baje un poco mas")



# --------------menus---------


# tacos=1
# pizza=2
# humitas=3
# cazuela=4

# print("elija una opcion de comida ")
# print("""tacos=1
# pizza=2
# humitas=3
# casuela=4""")
# op=int(input())
# if op==(1):
#     print("usted prefiere los tacos")
# elif (op==(2)):
#     print("usted prefiere la pizza")
# elif (op==(3)):
#     print("usted prefiere las humitas")
# elif (op==(4)):
#     print("usted prefiere la cazuela")
# else:


# suma=1
# resta=2
# multiplicacion=3
# division=4

# while True:
#     print("elija una opcion matematica ")
#     print("""suma=1
#     resta=2
#     multiplicacion=3
#     division=4
#     salir=5""")
#     op=int(input())
#     if op==(1):
#         print("usted prefiere la suma")
#         print("ingrese un numero")
#         num1=int(input())
#         print("ingrese un numero")
#         num2=int(input())
#         print(num1+num2)
#     elif (op==(2)):
#         print("usted prefiere la resta")
#         print("ingrese un numero")
#         num1=int(input())
#         print("ingrese un numero")
#         num2=int(input())
#         print(num1-num2)
#     elif (op==(3)):
#         print("usted prefiere la multiplicacion")
#         print("ingrese un numero")
#         num1=int(input())
#         print("ingrese un numero")
#         num2=int(input())
#         print(num1*num2)
#     elif (op==(4)):
#         print("usted prefiere la division")
#         print("ingrese un numero")
#         num1=int(input())
#         print("ingrese un numero")
#         num2=int(input())
#         print(num1/num2)
#     elif (op==(5)):
#         break
#     else:
#         print("elije otra opcion")

# comida=100

# while comida!=0:
#     print("aun tiene comida en su plato")
#     print("va a comer alguna cucharada? (si/no)")
#     verificacion=input()
#     if verificacion=="si":
#         print("a saco una cucharada")
#         comida=comida-25
#         print("a comido", comida , "%")
#         if comida==0:
#             print("he quedado satisfecho")
#             break
#     else:
#             print("usted no a terminado de comer")


# pasword=""
# print("ingrese su contraseña")
# pasword=input()

# while pasword != "colo colo":
#     print("su pasword es incorecto")
#     pasword=input()
# print("bienvenido garrero")

# def mostrar_menu():
#     print("\nMenú de opciones:")
#     print("1. Pago de Tarjeta de Crédito")
#     print("2. Simulación de Compras")
#     print("3. Salir")

# def realizar_pago(saldo):
#     try:
#         monto_pago = float(input("Ingrese el monto a pagar en la tarjeta de crédito: "))
        
#         if monto_pago < 0:
#             print("Error: El monto a pagar no puede ser negativo.")
#             return saldo
        
#         if monto_pago > saldo:
#             print("Error: El monto a pagar no puede exceder el saldo actual.")
#             return saldo
        
#         saldo -= monto_pago
#         print(f"Pago realizado correctamente. El saldo actual es: ${saldo:.2f}")
#         return saldo
    
#     except ValueError:
#         print("Error: Por favor ingrese un valor numérico válido.")
#         return saldo

# def realizar_compras(saldo):
#     while True:
#         try:
#             monto_compra = float(input("Ingrese el monto de la compra (o 0 para salir): "))
            
#             if monto_compra == 0:
#                 break
            
#             if monto_compra < 0:
#                 print("Error: El monto de la compra no puede ser negativo.")
#                 continue
            
#             saldo += monto_compra
#             print(f"Compra realizada por ${monto_compra:.2f}. El saldo actual es: ${saldo:.2f}")
        
#         except ValueError:
#             print("Error: Por favor ingrese un valor numérico válido.")
    
#     return saldo

# def main():
#     saldo = 100000  # Deuda inicial de la tarjeta
#     while True:
#         mostrar_menu()
#         try:
#             opcion = int(input("Seleccione una opción: "))
            
#             if opcion == 1:
#                 saldo = realizar_pago(saldo)
#             elif opcion == 2:
#                 saldo = realizar_compras(saldo)
#             elif opcion == 3:
#                 print("Saliendo del programa...")
#                 break
#             else:
#                 print("Error: Opción no válida. Intente nuevamente.")
#         except ValueError:
#             print("Error: Por favor ingrese un número entero válido.")

# if __name__ == "__main__":
#     main()


