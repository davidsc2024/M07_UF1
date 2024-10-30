#Ejercicio 10

import string

#Creamos la lista del abecedario
abecedario = list(string.ascii_lowercase)

#Eliminamos las letras en posiciones múltiples de 3
abecedario = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

#Convertimos la lista a tupla
abecedario_tupla = tuple(abecedario)

#Mostramos la lista y la tupla
print("Lista del abecedario modificada:", abecedario)
print("Tupla del abecedario modificada:", abecedario_tupla)
