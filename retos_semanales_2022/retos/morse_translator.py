#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.

import bs4
import requests
import re


URL = "https://es.wikipedia.org/wiki/C%C3%B3digo_morse"


def getWikiMorseCodes(wiki_url: str = URL) -> dict:
    try:
        response = requests.get(URL)
        soup = bs4.BeautifulSoup(response.text, features="html.parser")
        table = soup.find("table", {"border": "0", "cellspacing": "0"})
        characters = []
        codes = []

        for row in table.findAll('tr')[1:]:  # type: ignore
            characters.append(row.findAll('td')[0].text.replace("\n", ""))
            codes.append(row.findAll('td')[1].text.replace("\n", "").replace(
                " ", "").replace("·", ".").replace("—", "_"))
            characters.append(row.findAll('td')[3].text.replace("\n", ""))
            codes.append(row.findAll('td')[4].text.replace("\n", "").replace(
                " ", "").replace("·", ".").replace("—", "_"))
            characters.append(row.findAll('td')[6].text.replace("\n", ""))
            codes.append(row.findAll('td')[7].text.replace("\n", "").replace(
                " ", "").replace("·", ".").replace("—", "_"))

        natural_dictionary = {char: code for char, code in zip(characters, codes)}
        return natural_dictionary
    except Exception:
        return {
            'A': '._', 'N': '_.', '0': '_____', 'B': '_...', 'Ñ': '__.__', '1': '.____', 'C': '_._.', 'O': '___',
            '2': '..___', 'CH': '____', 'P': '.__.', '3': '...__', 'D': '_..', 'Q': '__._', '4': '...._', 'E': '.',
            'R': '._.', '5': '.....', 'F': '.._.', 'S': '...', '6': '_....', 'G': '__.', 'T': '_', '7': '__...',
            'H': '....', 'U': '.._', '8': '___..', 'I': '..', 'V': '..._', '9': '____.', 'J': '.___', 'W': '.__',
            '.': '._._._', 'K': '_._', 'X': '_.._', ',': '__..__', 'L': '._..', 'Y': '_.__', '?': '..__..',
            'M': '__', 'Z': '__..', '"': '._.._.'
        }


def translateMorse(text: str, dictionary: dict = getWikiMorseCodes()) -> str:
    if len(dictionary.values()) == 0 or not dict:
        print("""Empty Dictionary: cannot get morse alphabet, insert manually.
            \rget from: https://es.wikipedia.org/wiki/C%C3%B3digo_morse""")
        return ""
    if re.match(r'^\w+|" "*$', text):
        words = list(map(lambda word: list(word), text.upper().split(" ")))
        for word in words:
            i = 0
            while i < len(word):
                if word[i] not in dictionary.keys():
                    raise KeyError(f"{word[i]} not in dictionary")
                if word[i] == "C" and word[i + 1] == "H":
                    word[i] = dictionary["CH"]
                    word.pop(i + 1)
                else:
                    word[i] = dictionary[word[i]]
                i += 1
        translated_text = "  ".join(list(map(lambda word: " ".join(word), words)))
        return translated_text
    elif re.match(r'^\.+|\_+|" "*$', text):
        morse_dictionary = {code: char for char, code in dictionary.items()}
        words = list(map(lambda word: word.split(" "), text.split("  ")))
        for word in words:
            i = 0
            while i < len(word):
                if word[i] not in morse_dictionary.keys():
                    raise KeyError(f"{word[i]} not in dictionary")
                word[i] = morse_dictionary[word[i]]
                i += 1
        translated_text = " ".join(list(map(lambda word: "".join(word), words)))
        return translated_text
    else:
        return ""


if __name__ == "__main__":
    natural_morse = translateMorse("Hello, world. How are you?")
    morse_natural = translateMorse(natural_morse)
    print(natural_morse)
    print(morse_natural)
