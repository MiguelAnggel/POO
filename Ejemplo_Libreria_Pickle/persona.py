class Persona:
    def __init__(self, id: int, nombre: str, edad: int):
        """
        Crea una nueva instancia de la clase Persona.

        Args:
            id (int): El ID de la persona.
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """
        Devuelve una representación en cadena de la persona.

        Returns:
            str: La representación en cadena de la persona.
        """
        return "{} - {} ({})".format(self.id, self.nombre, self.edad)