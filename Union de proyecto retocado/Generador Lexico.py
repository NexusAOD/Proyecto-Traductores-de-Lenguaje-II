import re

from Pila import Pila
from Matriz import Matriz


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
    codigo = "a+b$"
#-------------------------------------------------------------------------------------
    tokens = lexer(codigo)
    mi_pila = Pila()     #Pila
    mi_matriz = Matriz() #Matriz
    x = 0
    y = 0
    f = 1
    palo =""
    a = 0

    vector = [
       # 0  1  2  3
        [2, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 3, 0, 0],
        [4, 0, 0, 0],
        [0, 0, 1, 0]
    ]

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

    for token, tipo_token in tokens:

        # Buscar el tipo en tipoT
        tipop = None
        for patron, tipo_valor in tipoT:
            if re.fullmatch(patron, tipo_token):
                tipop = tipo_valor
                break

        #if tipop is not None:
        #print(f"Token: {token}, Tipo token: {tipo_token}, Tipo: {tipop}")


        palo = codigo[a] + str(vector[y][x])
        y = vector[y][x]
        mi_pila.apilar(palo)


        if "+" in codigo[f]:
            x = 1
            f += 1
            a += 1
           

        elif codigo[f].isalpha() and all(letra.isalpha() or letra.isspace() for letra in codigo[f]):
            x = 0
            f += 1
            a += 1

        else:
            x = 2
        
        #print(mi_pila.cima())
        
        print("x = ", x)
        print("y = ", y)
        print("codigo = ", codigo[f])
        print(vector[y][x])
        print(mi_pila.cima())
    
    xp = 0
    yp = 5
    valor = mi_matriz.obtener_valor(yp, xp)
    print(f"El valor en las coordenadas ({xp}, {yp}) es: {valor}")

"""
#listar tokens
print("Lista de Tokens:")
for token, _ in tokens:
    print(token)
"""

if __name__ == "__main__":
    main()