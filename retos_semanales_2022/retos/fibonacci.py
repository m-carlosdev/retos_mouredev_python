#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...

def calcFibonacci(limit: int, a = 0, b = 1) -> None:
    if limit <= 0:
        return
    if limit == 1:
        print(a)
    else:
        print(a)
        aux = b
        b += a
        a = aux
        calcFibonacci((limit - 1), a, b)

if __name__=="__main__":
    calcFibonacci(50)
