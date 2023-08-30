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

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)
