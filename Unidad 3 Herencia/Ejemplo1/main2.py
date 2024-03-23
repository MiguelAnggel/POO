from ornitorrinco import Ornitorrinco
from murcielago import Murcielago
def main ():
    dracula = Murcielago(nombre= "Dracula",  
    especie = "Vampiro", edad = 500)
    dracula.comer()
    dracula.hacer_sonido()
    dracula.amamantar()
    dracula.dormir()
    dracula.volar()

    perry = Ornitorrinco('perry', 5)
    print(f'{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos')
    perry.poner_huevos()
    perry.poner_huevos()
    perry.poner_huevos()
    
    print(f'{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos')

if __name__ == "__main__":
    main()