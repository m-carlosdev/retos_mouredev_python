#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del
# lenguaje que lo hagan directamente.

def decToBin(num: int) -> str:
    if not num:
        return "0"

    binary_num = []

    while num > 0:
        binary_num.insert(0, str(num % 2))
        num //= 2
    return "".join(binary_num)


if __name__ == "__main__":
    print(decToBin(1567))
