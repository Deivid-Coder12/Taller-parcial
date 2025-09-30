class Motor: 
    def __init__(self, velocidad): 
        self.__velocidad = velocidad # refactor aquí 
    @property
    def velocidad(self):
        if (0<= self.__velocidad <=200):
            return self.__velocidad
        else:
           raise ValueError("la velocidad tiene que estar entre 0 y 200")
m=Motor(100)
print(m.velocidad)
