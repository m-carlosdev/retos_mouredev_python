#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.

def calcArea(polygon: str, a: float = 1, b: float = 1) -> float:
    if polygon not in ["rectangle", "square", "triangle"]:
        return
    if polygon == "rectangle" or polygon == "square":
        return a * b
    if polygon == "triangle":
        return a * b / 2


if __name__ == "__main__":
    triangle = calcArea("triangle", 3, 5)
    square = calcArea("square", 3, 3)
    rectangle = calcArea("rectangle", 5, 7)

    print("triangle area:", triangle)
    print("rectangle area:", rectangle)
    print("square area:", square)
