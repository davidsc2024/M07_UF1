#Ejercicio 2

#Creamos la tupla con los meses del año.
mesesAny = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    #Usamos un try except ValueError para controlar mejor el codigo frente a entradas no validas
    try:
        #Guardo la eleccion del usuario en un tipo entero
        eleccion = int(input("Escribe del 1 al 12 para visualizar los meses y 0 para salir: "))
        #Si la eleccion es 0 se cierra el código con el break
        if eleccion == 0:
            print("Saliendo del codigo.")
            break
        #Si la elección es entre 1 y 12 nos muestra los meses guardados en la tupla
        elif 1 <= eleccion <= 12:
            print("El mes seleccionado es:", mesesAny[eleccion - 1]) # - 1 para ajustar el indice
        #Sino se emite un mensaje de error
        else:
            print("Número no válido.\nEscribe del 1 al 12 para visualizar los meses y 0 para salir.")
    except ValueError:
        print("Por favor introduce un número válido.")