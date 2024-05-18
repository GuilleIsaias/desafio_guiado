from personaje import Personaje
from script import Script
import random

print("¡Bienvenido a Gran Fantasía!")
n_player = input("Por favor indique el nombre de su personaje:\n")
player = Personaje(n_player)
ORCO = Personaje("Orco")
s = Script()
status_player = f"NOMBRE: {player.get_nombre}\tNIVEL: {player.get_player_lvl}\tEXP: {player.exp}"
ORCO_status = f"NOMBRE: {ORCO.get_nombre}\tNIVEL: {ORCO.get_player_lvl}\tEXP: {ORCO.get_exp}"
print(status_player)
print(s.orco_aparece)
print(s.probabilidades50)
option = int(input("¿Que deseas hacer?\n1. Atacar \n2. Huir\n"))
if option == 1:
    while True:
        p_probabilidades = player.get_probabilidades(ORCO)
        if random.random() <= p_probabilidades:
            print(s.victoria)
            player.lvl_up(50)
            ORCO.lvl_up(-30)
        else:
            print(s.derrota)
            player.lvl_up(-30)
            ORCO.lvl_up(50)
        print(status_player)
        print(ORCO_status)
        if player.get_player_lvl == ORCO.get_player_lvl:
            print(s.probabilidades50)
        elif player.get_player_lvl > ORCO.get_player_lvl:
            print(s.probabilidades66)
        elif player.get_player_lvl < ORCO.get_player_lvl:
            print(s.get_probabilidades33)
        option = int(input("¿Que deseas hacer?\n1. Atacar \n2. Huir\n"))
        if option != 1:
            break
else: 
    print(s.huida)




    



