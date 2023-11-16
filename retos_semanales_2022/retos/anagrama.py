#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

import re
import unicodedata

def text_formatter(text: str) -> str:
    formatted_text = re.sub(r"\W", "", text).lower()
    formatted_text = unicodedata.normalize("NFKD", formatted_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return formatted_text

def isAnagram(text_1: str, text_2: str) -> bool:
    if (text_1 == text_2):
        return False
    text_1 = text_formatter(text_1)
    text_2 = text_formatter(text_2)

    return sorted(str(text_1)) == sorted(str(text_2))
