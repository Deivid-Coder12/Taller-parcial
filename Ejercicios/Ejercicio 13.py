class Usuario:
    def __init__(self, nombre):
        if isinstance(nombre, str): 
            self._nombre = nombre
        else:
            raise TypeError("El dato tiene que ser str")

    @property
    def nombre(self):
        return self._nombre

nombre = Usuario("s")
print(nombre.nombre)
