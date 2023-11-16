#  * Escribe una función que calcule si un número dado es un número de Armstrong
#  * (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información
#  * al respecto.

def is_armstrong(num: int) -> bool:
    number = str(num)
    armstrong_number = 0
    for char in number:
        armstrong_number += int(char) ** len(number)
    return armstrong_number == num
