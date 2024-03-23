import os

def main():
    # Obtenemos el directorio del archivo actual
    directorio = os.path.dirname(__file__)

    # Unimos el directorio actual con el nombre de los archivos
    # Esto nos da la ruta completa al archivo de origen y al archivo de destino
    archivo_origen = os.path.join(directorio, "entrada.txt")
    archivo_destino = os.path.join(directorio, "salida.txt")

    # Abrimos el archivo de origen en modo de lectura binaria
    with open(archivo_origen, "rb") as origen: #rb = lectura binaria
        # Abrimos el archivo de destino en modo de escritura binaria
        with open(archivo_destino, "wb") as destino: #wb = escritura binaria
            # Leemos el archivo de origen un byte a la vez
            while True:
                paquete = origen.read(1)
                # Si no hay más bytes para leer, salimos del bucle
                if not paquete:
                    break

                # Escribimos el byte leído en el archivo de destino
                destino.write(paquete)


if __name__ == "__main__":
    main()