#  * Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  * y retorne su resultado en milisegundos.

def time_converter(days: int = None, hours: int = None, minutes: int = None, seconds: int = None) -> int:
    milliseconds = 0
    if days:
        days = days * 24 * 60 * 60 * 1000
        milliseconds += days
    if hours:
        hours = hours * 60 * 60 * 1000
        milliseconds += hours
    if minutes:
        minutes = minutes * 60 * 1000
        milliseconds += minutes
    if seconds:
        seconds = seconds * 1000
        milliseconds += seconds
    return milliseconds


print(time_converter(days=9, minutes=45))
