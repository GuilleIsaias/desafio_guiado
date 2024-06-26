import math

class Personaje():

    def __init__(self, p_nombre):
        self.nombre = p_nombre
        self.player_level = 1
        self.exp = 0

    def estado(self):
        return self.nombre, self.player_level, self.exp

    @property
    def get_nombre(self):
        return self.nombre
    
    @property
    def get_player_lvl(self):
        return self.player_level
    
    @property
    def get_exp(self):
        return self.exp
    
    @get_nombre.setter
    def s_nombre(self, nombre: str):
        self.nombre = nombre

    @get_player_lvl.setter
    def s_lvl(self, lvl):
        self.player_level = lvl

    @get_exp.setter
    def s_exp(self, exp):
        self.exp = exp

    def lvl_up(self, p_exp: int):
        new_exp = p_exp + self.exp
        if new_exp < 0:
            self.exp = 0 
            if self.player_level > 1:
                self.exp = 100+new_exp
                self.player_level -= 1
        else:
            self.player_level += new_exp//100
            self.exp = new_exp%100

    def __lt__(self, other):
       return self.player_level < other.player_level
    
    def __gt__(self, other):
        return self.player_level > other.player_level
    
    def __eq__(self, other):
        return self.player_level == other.player_level
    
    def get_probabilidades(self, p_player):
        if self.__lt__(p_player):
            v_prob = 0.33
        elif self.__gt__(p_player):
            v_prob = 0.66
        elif self.__eq__(p_player): 
            v_prob = 0.5
        return v_prob  