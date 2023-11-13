from Matriz import Matriz

class R26: 
    #        R26 <Otro> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 37
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "Otro" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila