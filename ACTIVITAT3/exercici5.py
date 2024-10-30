#Ejercicio 5

#Pedimos al usuario que ingrese una frase
frase = input("Escribe una frase: ")

#Eliminamos los espacios y lo convertimos a una tupla
frase_sin_espacios = ''.join(frase.split())
tupla_frase = tuple(frase_sin_espacios)
print("Contenido de la tupla:", tupla_frase)

#Quitamos caracteres repetidos
frase_sin_repetidos = ''.join(sorted(set(frase_sin_espacios), key=frase_sin_espacios.index))
print("Frase sin caracteres repetidos:", frase_sin_repetidos)
