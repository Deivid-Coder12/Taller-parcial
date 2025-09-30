class Registro: 
    def __init__(self): 
        self.__items = ["obj.Escencial"] 

    def add(self, x): 
        self.__items.append(x) 

    @property
    def items(self):

        return tuple(self.__items)
r=Registro()
r.add("obj.modificable1")
r.add("obj.modificable2")
print(r.items)
