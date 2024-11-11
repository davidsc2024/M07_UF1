from create import create_usuario
from read import read_usuarios
from update import update_usuario
from delete import delete_usuario

def main():
    while True:
        print("\nMenú:")
        print("1. Crear usuario")
        print("2. Leer usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            descripcion = input("Descripción: ")
            sueldo = float(input("Sueldo: "))
            create_usuario(nombre, apellido, email, descripcion, sueldo)
        elif choice == '2':
            read_usuarios()
        elif choice == '3':
            user_id = int(input("ID del usuario para actualizar: "))
            nueva_descripcion = input("Descripción: ")
            nuevo_sueldo = input("Nuevo sueldo: ")
            nuevo_sueldo = float(nuevo_sueldo) if nuevo_sueldo else None
            update_usuario(user_id, nueva_descripcion, nuevo_sueldo)
        elif choice == '4':
            user_id = int(input("ID del usuario para eliminar: "))
            delete_usuario(user_id)
        elif choice == '5':
            break
        else:
            print("Elige una opción válida.")

if __name__ == "__main__":
    main()