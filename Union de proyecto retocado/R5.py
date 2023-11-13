from Matriz import Matriz

class R5: 
    #        R5 <Definicion> ::= <DefFunc> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Definicion = 26
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, Definicion) 
        parametro = "Definicion" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila