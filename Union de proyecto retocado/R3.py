from Matriz import Matriz

class R3: 
    # R3 <Definiciones> ::= <Definicion> <Definiciones> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Definiciones = 25
        mi_pila.desapilar()
        mi_pila.desapilar()
        #mi_pila.desapilar()
        #mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, Definiciones) 
        parametro = "Definiciones" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila