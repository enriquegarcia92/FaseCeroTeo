import re
from tabulate import tabulate


# Clase para representar un token
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


# Clase para representar la tabla de símbolos
class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def print(self):
        table_data = []
        for key, value in self.table.items():
            table_data.append([key, value.type, value.value])
        headers = ["Identificador", "Tipo", "Valor"]
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))


# Función para verificar si una cadena es una palabra reservada
def isReservedWord(word):
    reserved_words = ['new', 'switch', 'break', 'case', 'char',
                      'class', 'return', 'default', 'implements', 'double',
                      'else', 'extends', 'for', 'if', 'int']
    return word in reserved_words


# Función para analizar el token
def analyzeToken(token_string, line_number):
    if token_string.isdigit():
        return Token("Constante", token_string)
    elif token_string.startswith('"') and token_string.endswith('"'):
        return Token("Cadena de caracteres", token_string)
    elif isReservedWord(token_string):
        return Token("Palabra reservada", token_string)
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token_string):
        return Token("Identificador", token_string)
    elif re.match(r'^[\+\-\*/%]$', token_string):
        return Token("Operador", token_string)
    elif re.match(r'^[\(\)\{\}\[\];]$', token_string):
        return Token("Caracter de bloqueo", token_string)
    elif token_string == '=':
        return Token("Operador de asignación", token_string)
    elif token_string == '.':
        return Token("Punto", token_string)
    elif token_string == "'":
        return Token("Comilla simple", token_string)
    elif token_string == ':':
        return Token("Dos puntos", token_string)
    else:
        print(f"Error en la línea: {line_number} Token no válido: {token_string}")
        return None


# Función para analizar el código fuente
def analyzeSourceCode(source_code):
    symbol_table = SymbolTable()

    # Eliminación de comentarios del código fuente (tanto de línea como de bloque)
    source_code = re.sub(r'//.*?|/\*.*?\*/', '', source_code, flags=re.DOTALL)

    # Tokenización del código fuente
    tokens = re.findall(r'\".*?\"|\w+|[^\w\s]', source_code)

    # Iteración y agregación de los tokens a la tabla de símbolos
    line_number = 1
    for token_string in tokens:
        analyzed_token = analyzeToken(token_string, line_number)
        if analyzed_token is not None:
            symbol_table.insert(token_string, analyzed_token)
        else:
            return None
        if '\n' in token_string:
            line_number += 1

    return symbol_table


# Función para leer el código fuente desde un archivo
def readSourceCodeFromFile(filename):
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code


# Función principal
def main():
    filename = "example.java"
    source_code = readSourceCodeFromFile(filename)
    symbol_table = analyzeSourceCode(source_code)

    if symbol_table is not None:
        print("Elementos lexicográficos encontrados:")
        for key in symbol_table.table.keys():
            print(key)
        print("\nTabla de símbolos:")
        symbol_table.print()


if __name__ == '__main__':
    main()