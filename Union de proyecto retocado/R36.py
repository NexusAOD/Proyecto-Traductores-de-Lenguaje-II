from Matriz import Matriz

class R36: 
    #       R36 <Termino> ::= identificador 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 42
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "Termino" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila