#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#  * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

import re
import unicodedata


def isPalindrome(text: str) -> bool:
    formatted_text = re.sub(r"\W", "", text).lower()
    formatted_text = unicodedata.normalize("NFKD", formatted_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    reversed_word = ""
    n = 0
    while n < len(formatted_text):
        n += 1
        reversed_word += formatted_text[-n]

    return (reversed_word == formatted_text)

if __name__ == "__main__":
    texto = "Ána lleva al oso la avellana."
    texto2 = "hola mundo"
    texto3 = "Anita lava la tina"

    print(isPalindrome(texto))
