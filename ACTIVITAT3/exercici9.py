#Ejercicio 9

#Definimos la lista de asignaturas
asignaturas = ["Matemáticas", "Historia", "Ciencias", "Inglés", "Educación Física", "Arte"]
notas = []

#Pedimos al usuario las notas para cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota para {asignatura}: "))
    notas.append(nota)

#Mostramos las notas
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} ha sacado {notas[i]}")
