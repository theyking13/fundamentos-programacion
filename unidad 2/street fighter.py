import random
import time

      
def juego_de_pelas():    
    hp_jugador1 = 60
    hp_jugador2 = 60
    
    print("¡Comienza el juego de peleas!")
    turno = 1

    while hp_jugador1 > 0 and hp_jugador2 > 0:
        print(f"\nTurno {turno}")
        print(f"Jugador 1 HP: {hp_jugador1} | Jugador 2 HP: {hp_jugador2}")
        
        daño = random.randint(2, 10)
        if random.random() < 0.2:  
            daño = int(daño * 1.6)
            print("¡Jugador 1 hace un daño crítico!")
            time.sleep(2)
            print("*") 
        hp_jugador2 -= daño
        print(f"Jugador 1 inflige {daño} de daño.")
        if hp_jugador2 <= 0:
            print("\n¡Jugador 1 gana la pelea!")
            break
        
        daño = random.randint(2, 10)
        if random.random() < 0.2:  
            daño = int(daño * 1.6)
            print("¡Jugador 2 hace un daño crítico!")
            time.sleep(2)
            print("*") 
        hp_jugador1 -= daño
        print(f"Jugador 2 inflige {daño} de daño.")
        if hp_jugador1 <= 0:
            print("\n¡Jugador 2 gana la pelea!")
            break
        
        turno += 1

juego_de_pelas()