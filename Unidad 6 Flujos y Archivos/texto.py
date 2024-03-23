import os

def main():
    # Obtenemos el directorio del archivo actual
    directorio = os.path.dirname(__file__)

    # Unimos el directorio actual con el nombre de los archivos
    # Esto nos da la ruta completa al archivo de origen y al archivo de destino
    archivo_origen = os.path.join(directorio, "numeros.txt")
    archivo_destino = os.path.join(directorio, "salida.txt")

    # Abrimos el archivo de origen en modo de lectura binaria
    with open(archivo_origen, "r") as origen: #r = lectura
        # Abrimos el archivo de destino en modo de escritura binaria
        with open(archivo_destino, "w") as destino: #w = escritura
            # Leemos el archivo de origen un byte a la vez
            while True:
                caracter = origen.read(1)
                # Si no hay más bytes para leer, salimos del bucle
                if not caracter:
                    break
                
                try:
                    num =int(caracter)
                    destino.write(str(num*2))
                except ValueError:
                    destino.write(caracter)


if __name__ == "__main__":
    main()