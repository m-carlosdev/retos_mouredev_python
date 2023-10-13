#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.

import string


def wordsCount(text: str) -> dict:
    collection = {}
    text = text.lower().translate(
        str.maketrans("", "", string.punctuation + "¡¿")
    ).split()
    for word in text:
        if word not in collection.keys():
            collection[word] = 1
        else:
            collection[word] += 1
    return collection


if __name__ == "__main__":
    text = "un uno, dos dos, tres tres."
    print(wordsCount(text))
