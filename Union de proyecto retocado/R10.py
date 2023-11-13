from Matriz import Matriz

class R10: 
    #        R10 <Parametros> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 30
        num = mi_pila.cima()
        NodNum = int(num[-2:])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "Parametros" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila