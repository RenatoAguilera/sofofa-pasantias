palabra = str(input("Ingrese una frase con puntuaciones: ")) #input para ingresar una frase
palabra = palabra.replace(".", "") #replase para cambiar el una  por ""
palabra = palabra.replace(",", "")
palabra = palabra.replace("-", "")
palabra = palabra.replace("_", "")
palabra = palabra.replace("á", "")
palabra = palabra.replace("é", "")
palabra = palabra.replace("í", "")
palabra = palabra.replace("ó", "")
palabra = palabra.replace("ú", "")
palabra = palabra.replace("?", "")
palabra = palabra.replace("¡", "")
palabra = palabra.replace("¿", "")
palabra = palabra.replace("!", "")
print(palabra) #imprime la frase sin puntuaciones