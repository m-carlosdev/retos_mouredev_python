#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.

VOCALS = {
    "á": "Á",
    "é": "É",
    "í": "Í",
    "ó": "Ó",
    "ú": "Ú"
}


def title_string(string: str) -> str:
    words = string.split(" ")
    new_string = []
    for word in words:
        if (97 <= ord(word[0]) <= 122):
            word = word.replace(word[0], chr(ord(word[0]) - 32), 1)
        if word[0] in VOCALS.keys():
            word = word.replace(word[0], VOCALS[word[0]], 1)
        new_string.append(word)
    return " ".join(new_string)
