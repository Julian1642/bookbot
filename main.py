from stats import count_words, imprimir_diccionario, ordenar_diccionario
from stats import count_character
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    archivo = sys.argv[1]
    num_words = count_words(get_book_text(archivo))
    num_char = count_character(get_book_text(archivo))

    lista_ordenada = imprimir_diccionario(ordenar_diccionario(num_char))

    texto_template = get_book_text("./template")
    final_report = texto_template.format(
        num_words=num_words, lista_ordenada=lista_ordenada, archivo=archivo
    )

    print(final_report)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    main()
