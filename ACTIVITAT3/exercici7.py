#Ejercicio 7

#Creamos el diccionario vacío
contactos = {}

#Pedimos al usuario que ingrese contactos
while True:
    nombre = input("Introduce el nombre del contacto (o 'no' para terminar): ")
    if nombre.lower() == 'no':
        break
    edad = int(input(f"Introduce la edad de {nombre}: "))
    if nombre not in contactos:
        contactos[nombre] = edad
    else:
        print("Este nombre ya existe en el diccionario.")

print("Diccionario de contactos:", contactos)
