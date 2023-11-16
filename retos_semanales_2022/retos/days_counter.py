#  * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
#  * de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se
#  *   lanzará una excepción.

from datetime import datetime
import re


def count_days(date_1: str, date_2: str) -> int:
    DATE_PATTERN = r"^([0-9]){2}[/]([0-9]){2}[/]([0-9]){4}$"
    try:
        if not re.match(DATE_PATTERN, date_1) or not re.match(DATE_PATTERN, date_1):
            raise ValueError

        date_1 = datetime.strptime(date_1, "%d/%m/%Y")
        date_2 = datetime.strptime(date_2, "%d/%m/%Y")

        return abs((date_1 - date_2).days)
    except ValueError:
        return 0


print(count_days("10/12/2028", "11/12/2028"))
