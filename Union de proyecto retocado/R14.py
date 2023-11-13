from Matriz import Matriz

class R14: 
    #        R14 <BloqFunc> ::= { <DefLocales> } 
    def manipular_pila(self, mi_pila ):
        mi_matriz = Matriz()
        num = ""
        NodNum = 0
        defvar = 31
        mi_pila.desapilar()
        mi_pila.desapilar()
        mi_pila.desapilar()
        num = mi_pila.cima()
        NodNum = int(num)
        numMat = mi_matriz.obtener_valor(NodNum, defvar) 
        parametro = "BloqFunc" + str(numMat)
        mi_pila.apilar(parametro)

        return mi_pila