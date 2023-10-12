#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
from math import sqrt


def isPrime(number: int) -> bool:
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1, 101):
        if isPrime(i):
            print(i)
