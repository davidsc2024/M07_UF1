#Ejercicio 8

#Pedimos al usuario que ingrese 10 números
numeros = list(map(int, input("Introduce 10 números separados por espacios: ").split()))

#Calculamos la suma y la media
suma_total = sum(numeros)
media = suma_total / len(numeros)

#Añadimos la suma y la media a la lista
numeros.extend([suma_total, media])

#Mostramos la lista y los resultados
print("Lista con números, suma y media:", numeros)
print("Suma total:", suma_total)
print("Media:", media)
