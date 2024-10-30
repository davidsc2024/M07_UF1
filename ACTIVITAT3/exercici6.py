#Ejercicio 6

areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

#Imprimir el segundo elemento
print("Segundo elemento:", areas_pis[1])

#Imprimir el último elemento
print("Último elemento:", areas_pis[-1])

#Imprimir el área de la terraza
print("Área de la terrassa:", areas_pis[7])

#Imprimir del primer elemento al tercer elemento
print("Primer al tercer elemento:", areas_pis[:3])

#Imprimir del tercer elemento al último
print("Del tercer al último elemento:", areas_pis[2:])

#Imprimir el total de área de las dos habitaciones
total_habitaciones = areas_pis[5] + areas_pis[11]
print("Total área de las dos habitaciones:", total_habitaciones)

#Modificar el área del lavabo y mostrar la nueva lista
areas_pis[9] = 8.50
print("Nueva área del lavabo:", areas_pis)

#Añadir el área del "pati interior" y mostrar la nueva lista
areas_pis.extend(["Pati Interior", 2.78])
print("Lista con el pati interior:", areas_pis)

#Imprimir el total de área del piso
total_area = sum([areas_pis[i] for i in range(1, len(areas_pis), 2)])
print("Área total del piso:", total_area)
