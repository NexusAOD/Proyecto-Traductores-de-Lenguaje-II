from Matriz import Matriz

class R40: 
    #       R40 <LlamadaFunc> ::= identificador ( <Argumentos> ) 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 43
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "LlamadaFunc" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila