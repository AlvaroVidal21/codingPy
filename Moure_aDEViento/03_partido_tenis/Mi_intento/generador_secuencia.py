import random

def generador_secuencia(numero_de_juegos):
    secuencia = []
    for _ in range(numero_de_juegos):
        secuencia.append(random.choice(['p1', 'p2']))

    return secuencia
