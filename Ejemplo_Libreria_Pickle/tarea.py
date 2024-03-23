from persona import Persona


class Tarea:
    def __init__(self, id, descripcion, responsable: Persona):
        """
        Crea una instancia de la clase Tarea.

        Args:
            id (int): El identificador de la tarea.
            descripcion (str): La descripción de la tarea.
            responsable (Persona): El objeto Persona responsable de la tarea.
        """
        self.id = id
        self.descripcion = descripcion
        self.completada = False
        self.responsable = responsable

    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la tarea.

        Returns:
            str: La representación de la tarea.
        """
        icono = "✅" if self.completada else "❌"
        return f"{self.id}: {self.descripcion} ({icono}) @{self.responsable.nombre}"

    def cambiar_estado(self):
        """
        Cambia el estado de la tarea entre completada e incompleta.
        """
        self.completada = not self.completada