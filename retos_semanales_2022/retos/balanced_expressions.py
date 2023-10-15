#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def isBalanced(expression: str) -> bool:
    pairs = {"}": "{", ")": "(", "]": "["}
    stack = []
    for i in range(len(expression)):
        if expression[i] in pairs.values():
            stack.append(expression[i])
        if expression[i] in pairs.keys() and len(stack) == 0:
            return False
        elif expression[i] in pairs.keys() and len(stack) > 0:
            if stack[-1] == pairs[expression[i]]:
                stack.pop()
            else:
                return False
    return True


if __name__ == "__main__":
    print(isBalanced(""))
