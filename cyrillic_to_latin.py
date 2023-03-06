import pathlib

def romanization():
    cyrillic_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    latin_alphabet = ["a", "b", "v", "g", "d", "je", "jo", "ž", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "c", "č", "š", "šč", "'", "y", "'", "e", "ju", "ja",
        "A", "B", "V", "G", "D", "Je", "Jo", "Ž", "Z", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "F", "H", "C", "Č", "Š", "Šč", "'", "Y", "'", "E", "Ju", "Ja"]

    consonants = list("бвгджзйклмнпрстфхцчшщъь")

    file_data = pathlib.Path("in_cirillic.txt").read_text(encoding="utf-8")

    latin_out = ""

    i = 0

    for letter in file_data:
        if letter in cyrillic_alphabet:
            if (i > 0 and
                ((letter in ["ё", "Ё"] and file_data[i - 1].lower() in ["щ", "ч", "ш"]) or
                (letter in ["е", "Е"] and file_data[i - 1].lower() in consonants))):
                if (letter == "е"):
                    latin_out += "e"
                elif (letter == "Е"):
                    latin_out += "E"
                elif(letter == "ё"):
                    latin_out += "o"
                elif(letter == "Ё"):
                    latin_out += "O"
            else:
                if ((i > 0
                and file_data[i - 1] in cyrillic_alphabet
                and letter == letter.upper())
                or (letter == letter.upper()
                and i < len(file_data) - 1
                and file_data[i + 1] in cyrillic_alphabet
                and file_data[i + 1] == file_data[i + 1].upper())):
                    latin_out += latin_alphabet[cyrillic_alphabet.index(letter)].upper()
                else:
                    latin_out += latin_alphabet[cyrillic_alphabet.index(letter)]
        else:
            latin_out += letter
        i += 1

    pathlib.Path("out_latin.txt").write_text(latin_out, encoding="utf-8")


if __name__ == "__main__":
    romanization()