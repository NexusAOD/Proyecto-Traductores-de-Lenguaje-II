class Estado:

    def __init__(self):
        self.estado = None  # Inicializamos la palabra como None

    def almacenar_estado(self, estado):
        self.estado = estado

    def obtener_estado(self):
        return self.estado