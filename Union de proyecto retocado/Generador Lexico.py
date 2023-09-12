import re

from Pila import Pila



def lexer(input_string):
    keywords = ['if', 'else', 'while', 'for', 'int', 'float']
    operators = ['+', '-', '*', '/', '=', '==', '<', '>', '<=', '>=','&&','||','!=']
    symbols = ['(', ')', '{', '}', ',', ';']

    token_patterns = [
        (r'\b(' + '|'.join(keywords) + r')\b', 'Palabras reservadas'),
        (r'\b\d+\b', 'Entero'),
        (r'[+\-]', 'opSuma'),
        (r'[*/]', 'opMul'),
        (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'Identificador'),
        (r'==', 'opIgualdad'), 
        (r'!=', 'opIgualdad'), 
        (r'[()]', 'Parentecis'),
        (r'[{}]', 'Llave'),
        (r'[;]', 'Punto y coma'),
        (r'[|][|]', 'opOr'),
        (r'[&][&]', 'opAnd'),
        (r'[!]', 'opNot'),
        (r'[=<>]', 'opRelac'), 
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
    codigo = "a+b$"
    tokens = lexer(codigo)
    mi_pila = Pila()
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
        (r'Identificador', 0),  
        (r'opSuma', 5),
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
        print(f"Token: {token}, Tipo token: {tipo_token}, Tipo: {tipop}")


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
        #print(vector[y][x])
        #print(mi_pila.cima())
    




"""
#listar tokens
print("Lista de Tokens:")
for token, _ in tokens:
    print(token)
"""

if __name__ == "__main__":
    main()