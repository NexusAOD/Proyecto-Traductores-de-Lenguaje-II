import re

from Pila import Pila
from Matriz import Matriz
from MenuReglas import MenuReglas

def lexer(input_string):
    tipo = ['int', 'float', 'string']
    ifKW = ['if']
    whileKW = ['while']
    returnKW = ['return']
    elseKW = ['else']

    token_patterns = [
        (r'\b(' + '|'.join(ifKW) + r')\b', 'if'),
        (r'\b(' + '|'.join(whileKW) + r')\b', 'while'),
        (r'\b(' + '|'.join(returnKW) + r')\b', 'return'),
        (r'\b(' + '|'.join(elseKW) + r')\b', 'else'), 
        (r'\b(' + '|'.join(tipo) + r')\b', 'Tipo'),
        (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'identificador'),
        (r'\b\d+\.\d+\b', 'real'),
        (r'\b\d+\b', 'entero'),
        (r"'[^']*'", 'cadena'),
        (r'[+\-]', 'opSuma'),
        (r'[*/]', 'opMul'),
        (r'[=<>]', 'opRelac'),
        (r'[|][|]', 'opOr'),
        (r'[&][&]', 'opAnd'),
        (r'[!]', 'opNot'),
        (r'==', 'opIgualdad'),
        (r'[;]', 'Punto y coma'),
        (r'[,]', 'Coma'), 
        (r'[(]', 'ParentecisI'),
        (r'[)]', 'ParentecisD'),
        (r'[{]', 'LlaveI'),
        (r'[}]', 'LlaveD'),
        (r'[=]', 'Igual'),
        (r'[$]', 'final'), 
        (r'\s+', None)  # Ignorar espacios en blanco
    ]

    tokens = []

    while input_string:
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append((value, token_type))
                break
        
        if not match:
            print("Error: Carater no reconocido '{}'".format(input_string[0]))
            break

        input_string = input_string[len(match.group(0)):].lstrip()

    return tokens


def main():
# Ejemplo de uso
#-------------------------------------------------------------------------------------
    codigo = "int hola;$"
#-------------------------------------------------------------------------------------
    tokens = lexer(codigo)
    mi_pila = Pila()     #Pila
    mi_matriz = Matriz() #Matriz
    mis_reglas = MenuReglas() #aqui se administran las reglas
    NoPila = 0
    IncPila = 0
    mi_pila.apilar(IncPila)
    listaT = []
    listaN = []
    contador = 0
    ElemenListT = ""
    ElemenListN = 0
    num = ""

    tipoT = [
        (r'identificador', 0),
        (r'entero', 1),  
        (r'real', 2),  
        (r'cadena', 3),  
        (r'Tipo', 4),    
        (r'opSuma', 5),
        (r'opMul', 6),
        (r'opRelac', 7),
        (r'opOr', 8),
        (r'opAnd', 9),
        (r'opNot', 10),
        (r'opIgualdad', 11),
        (r'Punto y coma', 12),
        (r'Coma', 13),
        (r'ParentecisI', 14),
        (r'ParentecisD', 15),
        (r'LlaveI', 16),
        (r'LlaveD', 17),
        (r'Igual', 18),
        (r'if', 19),
        (r'while', 20),
        (r'return', 21),
        (r'else', 22),
        (r'final', 23), 
    ]

#------------------------------------------------------------------------------------------------------------------------------------
    for token, tipo_token in tokens:
        elementoT = token
        listaT.append(elementoT)
        # Buscar el tipo en tipoT
        tipop = None
        for patron, tipo_valor in tipoT:
            if re.fullmatch(patron, tipo_token):
                tipop = tipo_valor
                listaN.append(tipop)
                break
        #if tipop is not None:
        #print(f"Token: {token}, Tipo token: {tipo_token}, Tipo: {tipop}")

#-------------------------------------------------------------------------------------------------------------------------------------

    while NoPila != -1: 
        while contador < len(listaT):  
            ElemenListT = listaT[contador]
            # tipos= 4, 0, 12, 12, 23
            ElemenListN = int(listaN[contador])
            if ElemenListN == 0:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1
            
            elif ElemenListN == 1:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 2:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    contador += 1    
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    contador += 1

            elif ElemenListN == 3:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 4:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 5:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 6:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 7:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 8:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 9:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 10:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1
                                
            elif ElemenListN == 11:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1
                                
            elif ElemenListN == 12:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 13:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 14:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 15:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1
                                
            elif ElemenListN == 16:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 17:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 18:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 19:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 20:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 21:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1

            elif ElemenListN == 22:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -8:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])   
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    contador += 1
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])                     
                    contador += 1
            elif ElemenListN == 23:
                NoPila = mi_matriz.obtener_valor(NoPila, ElemenListN)
                if NoPila == -1:
                    print("Finalizado....")
                    contador += 1 
                elif NoPila > 0:
                    mi_pila.apilar(ElemenListT + str(NoPila))
                    pass
                elif NoPila < 0:
                    mi_pila = mis_reglas.select_option(NoPila, mi_pila)
                    num = mi_pila.cima()
                    NoPila = int(num[-1])    
                    pass            
            else:
                print("Error.....")
            print("Cima pila: ", mi_pila.cima(), "ElementT: ", ElemenListT, "Numero de matriz: ", NoPila, "Tipo: ", ElemenListN, )


"""  
#prueba de matriz---------------------------------------------------------------------------------------------
    x = 4
    y = 0
    valor = mi_matriz.obtener_valor(y, x)
    print(f"El valor en las coordenadas ({x}, {y}) es: {valor}")
#prueba de matriz---------------------------------------------------------------------------------------------

"""


if __name__ == "__main__":
    main()