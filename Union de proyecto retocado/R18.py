from Matriz import Matriz

class R18: 
    #        R18 <DefLocal> ::= <Sentencia> 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 34
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "DefLocal" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila