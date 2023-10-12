#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def reverseString(string: str) -> str:
    reversed_string = ""
    for i in range(1, len(string) + 1):
        reversed_string += string[-i]
    return reversed_string


if __name__ == "__main__":
    print(reverseString("Hola Mundo"))
