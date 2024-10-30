#Ejercicio 4

#Guardamos el string que introduce el usuario y lo dividimos con split por cada espacio, estos strings serán convertidos a enteros usando la funcion map(int, input), y a su vez también lo convertimos en una tupla con tuple().
numeros_usuario = tuple(map(int, input("Introduce 10 números separados por un espacio: ").split()))
print(numeros_usuario)