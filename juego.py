from personaje import Personaje
import random


print("¡Bienvenido a Gran Fantasía!")
n_player = input("Por favor indique el nombre de su personaje:\n")
player = Personaje(n_player)
print(f"NOMBRE: {player.get_nombre}\tNIVEL: {player.get_player_lvl}\tEXP: {player.get_exp}")
print("¡oh no!, ¡Ha aparecido un Orco!")
ORCO = Personaje("Orco")
print(f'Con tu nivel actual, tienes 50.0% de probabilidades de ganarle al Orco. \nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.')
option = input("¿Que deseas hacer?\n 1. Atacar \n2. Huir")






