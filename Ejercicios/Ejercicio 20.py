class ContadorSeguro:
    def __init__(self, n=0):
        self._n = n

    def inc(self):
        self._n += 1
        self.__log()   

    @property
    def n(self):
        return self._n

    def __log(self):
        print("tick")

c = ContadorSeguro()
c.inc()  
c.inc()  
print("Valor final:", c.n)
