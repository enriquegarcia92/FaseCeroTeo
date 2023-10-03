import os
import re
import sys

from tabulate import tabulate


# Clase para representar un token
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


# Clase para representar un nodo del árbol de búsqueda
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


# Clase para representar el árbol de búsqueda
class SymbolTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, value)
            else:
                self._insert(key, value, current_node.left)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, value)
            else:
                self._insert(key, value, current_node.right)
        else:
            current_node.value = value

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self._search(key, self.root)

    def _search(self, key, current_node):
        if key == current_node.key:
            return current_node.value
        elif key < current_node.key and current_node.left is not None:
            return self._search(key, current_node.left)
        elif key > current_node.key and current_node.right is not None:
            return self._search(key, current_node.right)
        else:
            return None

    def print(self):
        table_data = []
        self._print(self.root, table_data)
        headers = ["Identificador", "Tipo", "Valor"]
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))

    def _print(self, current_node, table_data):
        if current_node is not None:
            self._print(current_node.left, table_data)
            table_data.append([current_node.key, current_node.value.type, current_node.value.value])
            self._print(current_node.right, table_data)


# Función para verificar si una cadena es una palabra reservada
def isReservedWord(word):
    reserved_words = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                      'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'false', 'final', 'finally',
                      'float', 'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'long',
                      'native', 'new', 'null', 'package', 'private', 'protected', 'public', 'return', 'short',
                      'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient',
                      'true', 'try', 'void', 'volatile', 'while']
    return word in reserved_words


# Función que analiza el token
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
        print(f"Error en la línea {line_number}: Token no válido: {token_string}")
        return None


# Función para analizar el código fuente
def analyzeSourceCode(source_code):
    symbol_tree = SymbolTree()

    # Eliminar comentarios del código fuente
    source_code = re.sub(r'//.*?\n|/\*.*?\*/', '', source_code, flags=re.DOTALL)

    # Tokenize the source code
    tokens = re.findall(r'\".*?\"|\w+|[^\w\s]', source_code)

    # Iterate over the tokens and add them to the symbol tree
    line_number = 1
    for token_string in tokens:
        analyzed_token = analyzeToken(token_string, line_number)
        if analyzed_token is not None:
            symbol_tree.insert(token_string, analyzed_token)
        else:
            return None
        if '\n' in token_string:
            line_number += 1

    return symbol_tree


# Función para leer el código fuente desde un archivo
def readSourceCodeFromFile(filename):
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code


# Función principal
def main():
    if getattr(sys, 'frozen', False):  # Check if running as a PyInstaller executable
        script_dir = os.path.dirname(sys.executable)  # Use PyInstaller's special directory
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(script_dir, "example.java")
    source_code = readSourceCodeFromFile(filename)
    symbol_tree = analyzeSourceCode(source_code)

    if symbol_tree is not None:
        print("\nTabla de símbolos:")
        symbol_tree.print()
        input()

if __name__ == '__main__':
    main()
