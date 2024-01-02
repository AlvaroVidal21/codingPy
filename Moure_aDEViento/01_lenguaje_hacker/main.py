
RUTA_TXT= 'texto_hacker.txt'

DICCIONARIO_HACKER = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    'u': 'v',
    'b': '6',
    'g': '9',
    'h': '#',
    'j': 'y',
    't': '7',
    'm': '7w7',
    'y': 'j',
    'z': '2',
    'p' : '|*',
    's' : '5',
    'c' : '[',
    'd' : '|9'
}
DICCINARIO_NORMAL = {
    '4': 'a',
    '3': 'e',
    '1': 'i',
    '0': 'o',
    'v': 'u',
    '6': 'b',
    '9': 'g',
    '#': 'h',
    'y': 'j',
    '7': 't',
    '7w7': 'm',
    'j': 'y',
    '2': 'z',
    '|*': 'p',
    '5': 's',
    '[': 'c',
    '|9': 'd'
}

def input_text():
    input_text = input('Enter text: ')
    return input_text


def lng_hacker(text: str) -> str:
    """
    Función que transforma el texto ingresado a lenguaje hacker acorde al diccionario
    """
    
    texto_tranformado = text.lower()
    text_hacker = ""

    for letra in texto_tranformado:

        if letra in DICCIONARIO_HACKER.keys():
            text_hacker += DICCIONARIO_HACKER[letra]
        
        elif letra == ' ':
            text_hacker += ' '
        
        else:
            text_hacker += '!x'


    return text_hacker
            

def agregar_texto_a_txt(texto: str):
    """
    Función que agrega el texto transformado a un archivo de texto
    """
    with open('texto_hacker.txt', 'a', encoding='utf-8') as f:
        f.write(texto + '\n')


def transformar_texto_normal(texto: str) -> str:
    """
    Función que transforma el texto hacker a texto normal
    """
    texto_normal = ""

    for letra in texto:
        if letra in DICCINARIO_NORMAL.keys():
            texto_normal += DICCINARIO_NORMAL[letra]
        
        elif letra == ' ':
            texto_normal += ' '
        
        else:
            texto_normal += '!x'

    return texto_normal

def leer_texto_normal(archivo_txt):
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        texto = f.readlines() # Esto es una lista
        print(texto)

    for txt in texto:
        print('replace')
        txt.replace('\n', '')
        print(texto)

    for txt in texto:
        print('functransformar')
        transformar_texto_normal(txt)
        print(texto)

    return texto

def run():
   texto_normal = leer_texto_normal(RUTA_TXT)
   print(texto_normal)

if __name__ == '__main__': 
    run()