from symbolTableClass import readSourceCodeFromFile
from symbolTableClass import analyzeSourceCode


# Función principal
def main():
    filename = "javaExamples/example.java"
    source_code = readSourceCodeFromFile(filename)
    symbol_table = analyzeSourceCode(source_code)

    if symbol_table is not None:
        print("Elementos lexicográficos encontrados:")
        for key in symbol_table.table.keys():
            print(key)
        print("\nTabla de símbolos:")
        symbol_table.print()

    input("Press Enter to exit...")


if __name__ == '__main__':
    main()
