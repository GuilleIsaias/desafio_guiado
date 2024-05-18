from personaje import Personaje

class Script():
    def __init__(self) -> None:
        self.orco_aparece = "¡oh no!, ¡Ha aparecido un Orco!"
        self.probabilidades50 = f'Con tu nivel actual, tienes 50.0% de probabilidades de ganarle al Orco. \nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.'
        self.probabilidades33 = f'Con tu nivel actual, tienes 33.0% de probabilidades de ganarle al Orco. \nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.'
        self.probabilidades66 = f'Con tu nivel actual, tienes 66.0% de probabilidades de ganarle al Orco. \nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.'
        self.victoria = f'¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!'
        self.derrota = f'¡oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!'
        self.huida = f'¡has huido! El orco ha quedado atras.'
  
    @property
    def get_orco_aparece(self):
        return self.orco_aparece
    
    @property
    def get_probabilidades50(self):
        return self.probabilidades50
    
    @property
    def get_probabilidades33(self):
        return self.probabilidades33
    
    @property
    def get_probabilidades66(self):
        return self.probabilidades66
    
    @property
    def get_victoria(self):
        return self.victoria
    
    @property
    def get_derrota(self):
        return self.derrota
    
    @property
    def get_huida(self):
        return self.huida