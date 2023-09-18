import re

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
        for key, value in self.table.items():
            print(key, "->", value.type, ":", value.value)

# Función para verificar si una cadena es una palabra reservada
def isReservedWord(word):
    reservedWords = ["if", "else", "while", "for", "def", "return"]
    return word in reservedWords

# Función para analizar un token
def analyzeToken(tokenString):
    if tokenString.isdigit():
        return Token("Constant", tokenString)
    elif tokenString.startswith('"') and tokenString.endswith('"'):
        return Token("String", tokenString)
    elif isReservedWord(tokenString):
        return Token("Reserved Word", tokenString)
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', tokenString):
        return Token("Identifier", tokenString)
    elif re.match(r'^[\+\-\*/%]$', tokenString):
        return Token("Operator", tokenString)
    elif re.match(r'^[\(\)\{\}\[\]]$', tokenString):
        return Token("Block Character", tokenString)
    else:
        return None

# Función para analizar el código fuente
def analyzeSourceCode(sourceCode):
    symbolTable = SymbolTable()

    tokens = re.findall(r'\".*?\"|\'.*?\'|\w+|[^\w\s]', sourceCode)
    for tokenString in tokens:
        token = analyzeToken(tokenString)
        if token is not None:
            symbolTable.insert(tokenString, token)

    return symbolTable

# Función para leer el código fuente desde un archivo
def readSourceCodeFromFile(filename):
    with open(filename, 'r') as file:
        sourceCode = file.read()
    return sourceCode

# Función para leer el código fuente desde la entrada estándar
def readSourceCodeFromStdin():
    sourceCode = input("Ingrese el código fuente: ")
    return sourceCode

# Función principal
def main():
    sourceCode = readSourceCodeFromStdin()
    symbolTable = analyzeSourceCode(sourceCode)

    print("Elementos lexicográficos encontrados:")
    symbolTable.print()

if __name__ == '__main__':
    main()