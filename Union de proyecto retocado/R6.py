from Matriz import Matriz

class R6: 
    #        R6 <DefVar> ::= tipo identificador <ListaVar> ;
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 27
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "DefVar" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila