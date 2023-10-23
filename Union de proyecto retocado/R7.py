from Matriz import Matriz

class R7: 
    #        R7 <ListaVar> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        listvar = 28
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, listvar)        
        parametro = "ListaVar" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila