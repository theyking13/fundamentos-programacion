# import random
# def dado():
#     dado=random.randint(1,6)

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

import random

def jugar_ludo():
    print("bienvenido a jugar ludo.")
    print("el objetivo es llegar a 24. si te pasas, pierdes.")
    print("buena suerte.") 

    posicion_jugador_1=0
    posicion_jugador_2=0
    posicion_jugador_3=0
    turno=1

    while True:
        if turno % 3 == 1:
            jugador_actual="jugador 1"
            jugador_actual=posicion_jugador_1
        elif turno % 3 == 2:
            jugador_actual = "jugador 2"
            jugador_actual = posicion_jugador_2
        else:
            jugador_actual = "jugador 3"
            jugador_actual = posicion_jugador_3
        input(f"\n{jugador_actual}: presiona enter para lanzar dado...")
        dado = random.randint (1,6)
        print(f"{jugador_actual} a sacado un {dado}.")

        nueva_posicion = posicion_actual + dado

        if nueva_posicion > 24:
            print(f"{jugador_actual} se paso! estaba en {posicion_actual} y ahora tiene {nueva_posicion}.")
            print(f"¡{jugador_actual} ha perdido!")
            return
        elif nueva_posicion == 24:
            print(f"¡felicidades! {jugador_actual} ha llegado exactamente a 24. ¡gano el ludo!")
            return
        else:
            print(f"{jugador_actual} ahora esta en la {nueva_posicion}")
        
        if turno % 3 == 1:
            posicion_jugador_1 = nueva_posicion
        elif turno % 3 == 2:
            posicion_jugador_2 = nueva_posicion
        else:
            posicion_jugador_3 = nueva_posicion
        
        turno += 1

jugar_ludo()
