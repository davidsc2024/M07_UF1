from conn import get_cursor, conn

def update_usuario(usuario_id, nueva_descripcion=None, nuevo_salario=None):
    cursor = get_cursor()
    if nueva_descripcion:
        cursor.execute('UPDATE usuarios SET descripcion = %s WHERE id = %s', (nueva_descripcion, usuario_id))
    if nuevo_salario:
        cursor.execute('UPDATE usuarios SET sueldo = %s WHERE id = %s', (nuevo_salario, usuario_id))
    conn.commit()
    cursor.close()
    print("El usuario se ha actualizado..")
