class Cuenta: 
    def __init__(self, saldo): 
        self._saldo = 0 
        self.saldo = saldo 
    @property 
    def saldo(self):
        return self._saldo

    @saldo.setter 
    def saldo(self, value): 
        if value < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = value

c=Cuenta(100)
