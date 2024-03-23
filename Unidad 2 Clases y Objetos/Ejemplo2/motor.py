class Motor:
    
    def __init__(self, no_serie):
        self.no_serie = no_serie

    def encender(self):
        print("Encendiendo motor")

    def __str__(self):
        return f"motor: {self.no_serie}"