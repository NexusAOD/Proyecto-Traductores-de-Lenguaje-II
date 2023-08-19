import re

def lexer(input_string):
    keywords = ['if', 'else', 'while', 'for', 'int', 'float']
    operators = ['+', '-', '*', '/', '=', '==', '<', '>', '<=', '>=']
    symbols = ['(', ')', '{', '}', ',', ';']

    token_patterns = [
        (r'\b(' + '|'.join(keywords) + r')\b', 'PALABRA_CLAVE'),
        (r'\b\d+\b', 'NUMERO_ENTERO'),
        (r'[+\-*/=<>:]', 'OPERADOR'),
        (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'IDENTIFICADOR'),
        (r'[(),;]', 'SIMBOLO'),
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

# Ejemplo de uso
codigo = "if x > 0: resultado = 2 * x"
tokens = lexer(codigo)
for token, tipo_token in tokens:
    print(f"Token: {token}, Tipo: {tipo_token}")

print("\nLista de Tokens:")
for token, _ in tokens:
    print(token)
