#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

def isAnagram(word_1: str, word_2: str) -> bool:
    if (word_1 == word_2):
        return False
    return sorted(str(word_1)) == sorted(str(word_2))
