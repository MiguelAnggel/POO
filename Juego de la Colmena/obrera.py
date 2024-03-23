from abeja import Abeja
class Obrera(Abeja):

    def __init__(self):
        super().__init__()
        self.ataque = -1
        self.simbolo = "🐝"

    def esReina(self):
        super().esReina()
        return False
    
    