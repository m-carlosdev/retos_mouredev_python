#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.


ACTIONS = {
    "run": "_",
    "jump": "|"
}


def run(commands: str, track: str) -> bool:
    commands = commands.split(" ")
    track_step = list(track.replace(" ", ""))
    route = ""

    for command in list(set(commands)):
        if command not in ACTIONS.keys():
            raise ValueError("action not allowed")

    for chunk in list(set(track_step)):
        if chunk not in ACTIONS.values():
            raise ValueError("invalid track")

    if len(commands) != len(track_step):
        return False

    for i in range(len(track_step)):
        if ACTIONS[commands[i]] == track_step[i]:
            route += track_step[i] + ""
        else:
            if commands[i] == "jump":
                route += "x"
            if commands[i] == "run":
                route += "/"
        print("\n")
        print(route)
    return route == track.replace(" ", "")
