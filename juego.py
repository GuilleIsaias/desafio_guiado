from personaje import Personaje
import random


print("¡Bienvenido a Gran Fantasía!")
n_player = input("Por favor indique el nombre de su personaje:\n")
player = Personaje(n_player)
print(f"NOMBRE: {player.get_nombre}\tNIVEL: {player.get_player_lvl}\tEXP: {player.get_exp}")
print("¡oh no!, ¡Ha aparecido un Orco!")
ORCO = Personaje("Orco")


