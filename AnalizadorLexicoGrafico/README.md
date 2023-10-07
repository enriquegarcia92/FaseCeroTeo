# Integrantes:

García Arévalo, José Enrique 00093619
      Hernández García, Rodrigo Anibal 00050519
      López Henríquez, Guillermo Daniel 00026018
      Cruz Cader, Miguel Alejandro 00019018
      Escobar Hernandez, Luis Gustavo 00091318
         Alejandro Enrique Rivera  Vasquez 00011218

Este documento presenta el desarrollo de un software tokenizador implementado en Python como parte de un proyecto de la materia de teoría de lenguajes de programación. El objetivo principal del software es realizar un análisis léxico preciso en programas escritos en Python, identificando y clasificando elementos léxicos como identificadores, palabras reservadas, operadores y constantes durante el proceso de compilación.

## El software se compone de varias clases y funciones clave:

1.  Clase Token: Representa elementos léxicos en un programa y tiene atributos "type" para el tipo de token y "value" para su contenido. Los tipos pueden ser constantes, palabras clave, identificadores, operadores, entre otros.
    
2.  Clase SymbolTable: Representa la tabla de símbolos de un programa y almacena información sobre identificadores. Ofrece métodos para insertar y mostrar identificadores.
    
3.  Función isReservedWord(word): Comprueba si una cadena es una palabra reservada en Python.
    
4.  Función analyzeToken(token_string): Analiza un token representado como una cadena y devuelve un objeto Token con su tipo y valor correspondientes.
    
5.  Función analyzeSourceCode(source_code): Analiza el código fuente Python, lo limpia de comentarios y construye una tabla de símbolos.
    
6.  Función readSourceCodeFromFile(filename): Lee el código fuente desde un archivo especificado.

## Ejecucion    

La ejecución del programa se realiza desde el archivo "main.py". Se importa la clase SymbolTable y se realiza el análisis léxico del código fuente. Los resultados se presentan en una tabla.

**Con ejecutable directo:**

Paso 1: En el administrador de archivos navega hasta la ubicación donde tienes guardado el archivo main.exe (en la carpeta: AnalizadorLexicoGrafico).

Paso 2: Darle doble click al archivo main.exe y si aparece una ventana emergente darle click al botón “run” o ejecutar.

Paso 3: Para salir del programa puedes darle click a Enter y esto terminará el proceso.

**Nota**: para ejecutar un código diferente de Java a los ejemplos que se ponen se debe de insertar dicho archivo “.java” en la carpeta: javaExamples y especificar en el main.py en la variable filename la ruta de ese nuevo archivo, ejemplo:

    filename = "javaExamples/example.java"

