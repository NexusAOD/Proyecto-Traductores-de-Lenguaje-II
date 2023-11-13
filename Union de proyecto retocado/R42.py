from Matriz import Matriz

class R42: 
    #        R42 <SentenciaBloque> ::= <Bloque> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 44
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "SentenciaBloque" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila