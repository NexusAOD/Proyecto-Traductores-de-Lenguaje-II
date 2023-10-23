from Matriz import Matriz

class R2: 
    #        R2 <Definiciones> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Definiciones = 25
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Definiciones)        
        parametro = "Definiciones" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila