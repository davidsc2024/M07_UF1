#Ejercicio 11

#Diccionario con divisas y símbolos
divisas = {
    "Euro": "€",
    "Dólar": "$",
    "Libra": "£",
    "Yen": "¥"
}

#Pedimos al usuario que ingrese una divisa
divisa = input("Introduce una divisa: ")

#Mostramos el símbolo si existe en el diccionario
if divisa in divisas:
    print("El símbolo de la divisa es:", divisas[divisa])
else:
    print("La divisa no está en el diccionario.")
