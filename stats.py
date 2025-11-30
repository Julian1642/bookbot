def count_words(string):
    i = 0
    for _ in string.split():
        i += 1
    return i


def count_character(text):
    alfabeto = {}
    for letra in text:
        minuscula = letra.lower()
        if minuscula in alfabeto:
            alfabeto[minuscula] += 1
        else:
            alfabeto[minuscula] = 1
    return alfabeto


def ordenar_diccionario(diccionario):
    lista_diccionarios = []
    for caracter, numero in diccionario.items():
        if caracter.isalpha():
            aux = {"char": caracter, "num": numero}
            lista_diccionarios.append(aux)

    lista_diccionarios.sort(key=lambda item: item["num"], reverse=True)
    return lista_diccionarios


def imprimir_diccionario(lista):
    lista_strings = []
    for diccionario in lista:
        lista_strings.append(f"{diccionario['char']}: {diccionario['num']}")

    diccionario_impreso = "\n".join(lista_strings)

    return diccionario_impreso
