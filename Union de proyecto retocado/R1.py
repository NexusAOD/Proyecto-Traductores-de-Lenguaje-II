from Matriz import Matriz

class R1: 
    # R1 <programa> ::= <Definiciones> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        programa = 24
        mi_pila.desapilar()
        #mi_pila.desapilar()
        #mi_pila.desapilar()
        #mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, programa) 
        parametro = "programa" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila