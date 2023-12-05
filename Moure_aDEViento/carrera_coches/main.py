import random
import time
import os


# Create track
def create_track(track_length: int) -> (list, list):
    """
    Crea una pista de carreras con árboles, coches y una meta.

    Args:
        track_length (int): Longitud de la pista.

    Returns:
        tuple: Una tupla que contiene las pistas del primer y segundo coche.
    """
    def add_trees(track: list) -> list:
        """
        Agrega árboles a la pista de carreras.

        Args:
            track (list): Pista de carreras.

        Returns:
            list: Pista de carreras con árboles agregados.
        """
        number_tress = random.randint(1, 4)

        for _ in range(number_tress):
            position_tree = random.randint(1, track_length - 1)
            track[position_tree] = '🎄'

        return track

    track = ['-'] * track_length
    track_1, track_2 = add_trees(track.copy()), add_trees(track.copy())

    track_1.append('🚗')
    track_2.append('🚙')

    track_1.insert(0, '🏁')
    track_2.insert(0, '🏁')

    return (track_1, track_2)


def print_race(track1: list, track2: list):
    """
    Imprime la carrera en la consola.

    Args:
        track1 (list): Pista del primer coche.
        track2 (list): Pista del segundo coche.
    """

    # Clear console in Windows 11
    os.system('cls')
    print("".join(track1))
    print("".join(track2))




# Winner car
def check_race_winner(position_1: int, position_2: int):
    if position_1 == 0 and position_2 == 0:
        print("\n")
        print("Empate")

    elif position_1 == 0:
        print("\n")
        print("Gana el coche 🚗")

    elif position_2 == 0:
        print("\n")
        print("Gana el coche 🚙")

# Principal function of the program 
def race(track_length: int):
    """
    Inicia una carrera en una pista de carreras.

    Args:
        track_length (int): Longitud de la pista.
    """
    track_1, track_2 = create_track(track_length)

    print_race(track_1, track_2)

    # Positions
    position_1, position_2 = len(track_1) - 1, len(track_2) - 1

    # Crasheds cars
    crashed_1, crashed_2 = False, False

    print(f'{position_1} - {position_2}')

    while position_1 > 0 and position_2 > 0:

        # Timer
        time.sleep(1)

        # Reset cars
        track_1[position_1] = '-'
        track_2[position_2] = '-'

        # Move cars
        position_1 -= 0 if crashed_1 else random.randint(1, 3)
        position_2 -= 0 if crashed_2 else random.randint(1, 3)

        # Reset crasheds cars
        crashed_1, crashed_2 = False, False

        # Conditions
        position_1 = 0 if position_1 < 0 else position_1
        position_2 = 0 if position_2 < 0 else position_2
        print(f'R: {position_1} - A: {position_2}')

        # How we know that car crashed with a tree?
        if track_1[position_1] == '🎄':
            crashed_1 = True

        if track_2[position_2] == '🎄':
            crashed_2 = True

        track_1[position_1] = '🚬' if crashed_1 else '🚗'
        track_2[position_2] = '🚬' if crashed_2 else '🚙'

        print_race(track_1, track_2)
        check_race_winner(position_1, position_2)


def run():
    """
    Función principal que inicia la carrera con una longitud de pista de 20.
    """
    race(30)


if __name__ == '__main__':
    run()
