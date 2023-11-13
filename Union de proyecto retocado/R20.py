from Matriz import Matriz

class R20: 
    #        R20 <Sentencias> ::= <Sentencia> <Sentencias> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 35
        mi_pila.desapilar()
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "Sentencias" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila