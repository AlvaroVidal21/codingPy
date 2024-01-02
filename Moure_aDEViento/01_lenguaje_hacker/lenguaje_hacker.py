
leet_dict = { 
    "A":"4",
    "B":"I3",
    "C":"[",
    "D":")",
    "E":"3",
    "F":"|=",
    "G":"&",
    "H":"#",
    "I":"1",
    "J":",_|",
    "K":">|",
    "L":"1",
    "M":"JVI",
    "N":"^/",
    "O":"0",
    "P":"|*",
    "Q":"(_,)",
    "R":"I2",
    "S":"5",
    "T":"7",
    "U":"(_)",
    "V":"|/",
    "W":"w",
    "X":"><",
    "Y":"j",
    "Z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o"
}


def leet_translator(text: str) -> str: # text = "Hola mundo"
    leet_text = ""

    for word in text: # Por cada letra del texto iteramos
        word_mayus = word.upper() 
        if word_mayus in leet_dict.keys(): # Si la letra está en el diccionario 
            leet_text += leet_dict[word_mayus] # Agregamos la letra traducida al texto 
        else: # para espacios vacíos o carácteres no encontrados en el diccionario
            leet_text += word_mayus

    return leet_text

def run():
    texto_translate = leet_translator("Hola mundo")

    print(f'Texto: {texto_translate}')

if __name__ == '__main__':
    run()
