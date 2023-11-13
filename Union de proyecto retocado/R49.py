from Matriz import Matriz

class R49: 
    #        R49 <Expresion> ::= <Expresion> opIgualdad <Expresion> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 45
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "Expresion" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila