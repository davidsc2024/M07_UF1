from conn import get_cursor, conn

def create_usuario(first_name, last_name, email, description, salary):
    cursor = get_cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre, apellido, email, descripcion, sueldo)
        VALUES (%s, %s, %s, %s, %s)
    ''', (first_name, last_name, email, description, salary))
    conn.commit()
    cursor.close()
    print("El usuario se ha creado.")
