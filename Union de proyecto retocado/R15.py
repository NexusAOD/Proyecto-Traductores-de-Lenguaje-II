from Matriz import Matriz

class R15: 
    #        R15 <DefLocales> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 33
        num = mi_pila.cima()
        NodNum = int(num[-2:])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "DefLocales" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila