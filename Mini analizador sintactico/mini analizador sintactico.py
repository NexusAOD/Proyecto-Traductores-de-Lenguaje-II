import re
#----------------------------------------------------------------------------------------------------
#clase pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def tamaño(self):
        return len(self.items)

#-----------------------------------------------------------------------------------------------
#Analizador Lexico
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
codigo = "hola+mundo"
tokens = lexer(codigo)


#---------------------------------------------------------------------------
# Crear una instancia de la clase Pila
mi_pila = Pila()

d = 2


print("\nLista de Tokens:")


print("   Pila   |   Entrada   |   Salida   ")

for token, _ in tokens:  
    mi_pila.apilar(token)

    if token in codigo:
        codigo = codigo.replace(token, "", 1) 
        print(mi_pila.cima(),"       ", codigo,"        ", "  d", d)
        d += 1