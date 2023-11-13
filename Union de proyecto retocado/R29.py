from Matriz import Matriz

class R29: 
    #        R29 <ValorRegresa> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 39
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "ValorRegresa" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila