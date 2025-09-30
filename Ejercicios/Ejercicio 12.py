class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)

    @property
    def temperatura_c(self):
        return self._c

    @property
    def temperatura_f(self):
        return (self._c * 9/5) + 32
    

t = Termometro(input("Ingrese el valor en grados celcius"))

print(f"En celcius es {t.temperatura_c} y en farenheits es {t.temperatura_f}")
