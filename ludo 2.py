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


import random

hp_jugador1 = 60
hP_jugador2= 60

def daño():
    return random.randint(2,10)

print("bienvenido al street fighter de phyton")
golpe = daño()
turno=1
while hp_jugador1 > 0 and hP_jugador2:
    print(f"\nturno {turno}")
    print(f"jugador 1 hp {hp_jugador1} 
          jugador 2 hp: {hP_jugador2} ")
    if random.random < 0.2:
        daño=int(daño * 1.6)
        print("jugador1 hace un daño critico   ")
    
     

