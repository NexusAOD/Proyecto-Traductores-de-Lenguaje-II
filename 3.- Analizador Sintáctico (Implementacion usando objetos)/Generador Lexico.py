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
    codigo = "/ == != || && a+b+c+d+e+f mundo86 ( { "
    tokens = lexer(codigo)

    for token, tipo_token in tokens:
        print(f"Token: {token}, Tipo: {tipo_token}")


    mi_pila = Pila()



"""
#listar tokens
print("Lista de Tokens:")
for token, _ in tokens:
    print(token)
"""

if __name__ == "__main__":
    main()