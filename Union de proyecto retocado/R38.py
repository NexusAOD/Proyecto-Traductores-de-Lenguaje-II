from Matriz import Matriz

class R38: 
    #       R38 <Termino> ::= real 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 42
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "Termino" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila