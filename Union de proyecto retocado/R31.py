from Matriz import Matriz

class R31: 
    #        R31 <Argumentos> ::= \e
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 40
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "Argumentos" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila