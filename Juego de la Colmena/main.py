from abeja import Abeja
from zangano import Zangano
from obrera import Obrera
from larva import Larva
from reina import Reina
from jugador import Jugador
import random

def impresionTablero(tablero):
    for i, abeja in enumerate(tablero):
        if abeja is None:
            print(f"{i + 1}, ")
        else:
            if abeja.visitado:
                print(f"Encontraste:{abeja.simbolo} ")


def generaColmenas(tamaño_colmena):
    poblacion = []
    for _ in range(tamaño_colmena):
        num_aleatorio = random.randint(3, 5) #Genera numero aleatorio entre 3 y 5
        if num_aleatorio in [1, 3]:
            poblacion.append(Larva())
            poblacion.append(Zangano())
        elif num_aleatorio in [4, 6]:
            poblacion.append(Obrera())
        else:
            poblacion.append(Zangano())
            
    return poblacion

def iniciar_juego():
    tamaño_colmena = random.randint(1, 25) 
    print("Numero Aleatorio: ", tamaño_colmena)

    colmena = generaColmenas(tamaño_colmena)
    posicion_reina = random.randint(1, tamaño_colmena)
    colmena[posicion_reina - 1] = Reina()
    jugador = Jugador()
    tablero = [None] * tamaño_colmena

    #Ciclo while que evalua la vida del jugador 
    while jugador.vida > 0:
        
        print(f"Vida actual del jugador: {jugador.vida}")
        print("\nTablero actual:")
        impresionTablero(tablero)

        print("\n")

        #exepciones y condiciones
        try:
            seleccion = int(input(f"Elige una posicion (Entre 1 y {tamaño_colmena}): ")) - 1
            if tablero[seleccion] is not None:
                print("Ya visitaste este espacio, elige otro")
                continue
            abeja = colmena[seleccion]
            abeja.visitado = True
            tablero[seleccion] = abeja
            if abeja.esReina():
                print("=== Encontaste a la Abeja Reina, Ganaste el juego ===")
                break #Rompe
            else:
                jugador.vida += abeja.ataque
                if jugador.vida <= 0:
                    print(f"=== Perdiste el juego ,No tienes mas vida. ===")
                    break
        except (ValueError, IndexError):
            print("Selecciona una posicion adecuada")

if __name__ == '__main__':
    #IMPRESIONES 
    print("\t === JUEGO DE LA COLMENA ===")
    print("\n")
    print("NIVEL DE DAÑO DE LAS ABEJAS:")
    print("👑 Abeja Reina: Si encuentras a la reina ganas")
    print("🐛 Larva: Las Larvas no disminuye tu vida")
    print("🐝 Obrera: Las Obreras disminuyen -1 punto de vida")
    print("☢️🐝 Zangano: Los Zanganos disminuyen -2 puntos de vida")
    print("\n")
    
    iniciar_juego()




