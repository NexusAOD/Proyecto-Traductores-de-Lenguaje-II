from Matriz import Matriz

class R19: 
    #        R19 <Sentencias> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 35
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "DefLocales" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila