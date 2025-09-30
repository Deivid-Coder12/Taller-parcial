class _Repositorio: 
    def __init__(self): 
        self._datos = {} 

    def guardar(self, k, v): 
        self._datos[k] = v 


    def _dump(self): 
        return dict(self._datos) 
    
class Servicio: 
    def __init__(self): 
        self.__repo = _Repositorio() 

    def guardar(self, k, v):
        self.__repo.guardar(k,v)

s=Servicio()
s.guardar("animal", "raton")
