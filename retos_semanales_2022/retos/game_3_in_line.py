#  * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#  * y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#  *   O si han ganado los 2.
#  * Nota: La matriz puede no estar totalmente cubierta.
#  * Se podría representar con un vacío "", por ejemplo.

matriz = [["O", "O", "O"], ["X", "X", "O"], ["O", "X", "X"]]

combinations = [
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]
]


def check_winner(matrix: list, combinations: list) -> str:
    plays = []
    combo = []
    winner = []
    for combination in combinations:
        if len(combo) >= 2:
            plays.append(combo.copy())
            combo.clear()
        for position in combination:
            x = position[0]
            y = position[1]
            combo.append(matriz[x][y])
    revision = list(map(set, plays))
    for element in revision:
        if len(element) < 2:
            winner.append(list(element)[0])
    if not winner:
        return "Empate"
    if len(winner) > 1:
        return "Nulo"
    return winner[0]


print(check_winner(matriz, combinations))
