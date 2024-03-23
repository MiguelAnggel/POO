from abeja import Abeja
class Zangano(Abeja):

    def __init__(self):
        super().__init__()
        self.ataque = -2
        self.simbolo = "☢️🐝"

    def esReina(self):
        super().esReina()
        return False




