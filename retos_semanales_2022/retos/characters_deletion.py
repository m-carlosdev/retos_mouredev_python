#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.

def delChars(str_1: str, str_2: str) -> None:
    out_1 = "".join(set(str_1).difference(str_2))
    out_2 = "".join(set(str_2).difference(str_1))
    print(out_1, out_2)


if __name__ == "__main__":
    delChars("hola", "mundo")

