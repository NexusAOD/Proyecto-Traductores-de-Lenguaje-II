from Matriz import Matriz

class R33: 
    #        R33 <ListaArgumentos> ::= \e 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        Hor = 41
        num = mi_pila.cima()
        NodNum = int(num[-1])
        numMat = mi_matriz.obtener_valor(NodNum, Hor)        
        parametro = "ListaArgumentos" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila