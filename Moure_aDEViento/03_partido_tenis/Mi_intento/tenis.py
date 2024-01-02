import time
from generador_secuencia import generador_secuencia
from pantalla_ganador import pantalla_ganador as pg


NUMERO_DE_JUEGOS = 800

PUNTUACIONES = [0, 15, 30, 40]

TIEMPO_DE_ESPERA = 0


def analizador_de_juego(secuencia):
    p1 = {"puntaje" : 0}
    p2 = {"puntaje" : 0}

    for ganador in secuencia: # ["p1", "p1", "p2"]
        if ganador == "p1":
            pg("p1")
            p1 = asignador_de_puntos(p1) # return {"puntaje" : 15}
            if p1["puntaje"] == p2["puntaje"]:  
                print(f'Deuce: p1: {p1["puntaje"]}, p2: {p2["puntaje"]}')
            else:
                print(f'p1: {p1["puntaje"]}, p2: {p2["puntaje"]}')
            time.sleep(TIEMPO_DE_ESPERA)
        else:
            pg("p2")
            p2 = asignador_de_puntos(p2)
            if p1["puntaje"] == p2["puntaje"]:
                print(f'Deuce: p1: {p1["puntaje"]}, p2: {p2["puntaje"]}')
            else:
                print(f'p1: {p1["puntaje"]}, p2: {p2["puntaje"]}')
            time.sleep(TIEMPO_DE_ESPERA)

    return p1, p2


def asignador_de_puntos(jugador: dict) -> dict:
    if jugador["puntaje"] == 0:
        jugador["puntaje"] = 15

    elif jugador["puntaje"] == 15:
        jugador["puntaje"] = 30

    elif jugador["puntaje"] == 30:
        jugador["puntaje"] = 40
    
    elif jugador["puntaje"] == 40:
        jugador["puntaje"] += 5

    else:
        jugador["puntaje"] += 2

    
    return jugador


def asignador_de_ganador(p1, p2):
    if p1["puntaje"] > p2["puntaje"]:
        return "ganador: p1"
    elif p1["puntaje"] < p2["puntaje"]:
        return "ganador: p2"
    else:
        return "empate"




def run():
    secuencia_de_juego = generador_secuencia(NUMERO_DE_JUEGOS)

    p1, p2 = analizador_de_juego(secuencia_de_juego)

    resultado = asignador_de_ganador(p1, p2)
    print(resultado)

if __name__ == '__main__':
    run()

