class Terminal:

    def __init__(self):
        self.Terminal = None  # Inicializamos la palabra como None

    def almacenar_Terminal(self, Terminal):
        self.Terminal = Terminal

    def obtener_Terminal(self):
        return self.Terminal