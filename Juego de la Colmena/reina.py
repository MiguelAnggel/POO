from abeja import Abeja
class Reina(Abeja):

    def __init__(self):
        super().__init__()
        self.ataque = 0
        self.simbolo = "👑"

    def esReina(self):
        return True

    
    
