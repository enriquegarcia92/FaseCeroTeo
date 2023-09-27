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
    reserved_words = ['as', 'break', 'class', 'continue', 'do', 'else', 'false', 'for', 'fun', 'if', 'in', 'interface',
                     'is', 'null', 'object', 'package', 'return', 'super', 'this', 'throw', 'true', 'try', 'typealias',
                     'typeof', 'val', 'var', 'when', 'while']
    return word in reserved_words


# Función que analiza el token
def analyzeToken(token_string):
    if token_string.isdigit():
        return Token("Constante", token_string)
    elif token_string.startswith('"') and token_string.endswith('"'):
        return Token("String", token_string)
    elif isReservedWord(token_string):
        return Token("Palabra Reservada", token_string)
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token_string):
        return Token("Identificador", token_string)
    elif re.match(r'^[\+\-\*/%]$', token_string):
        return Token("Operador", token_string)
    elif re.match(r'^[\(\)\{\}\[\]]$', token_string):
        return Token("Caracter de bloqueo", token_string)
    else:
        return None


# Función para analizar el código fuente
def analyzeSourceCode(source_code):
    symbol_table = SymbolTable()

    tokens = re.findall(r'\".?\"|\'.?\'|\w+|[^\w\s]', source_code)
    for tokenString in tokens:
        token = analyzeToken(tokenString)
        if token is not None:
            symbol_table.insert(tokenString, token)

    return symbol_table


# Función para leer el código fuente desde un archivo
def readSourceCodeFromFile(filename):
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code


# Función principal
def main():
    filename = "example.kt"
    source_code = readSourceCodeFromFile(filename)
    symbol_table = analyzeSourceCode(source_code)

    print("Elementos lexicográficos encontrados:")
    symbol_table.print()


if __name__ == '__main__':
    main()
