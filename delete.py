from conn import get_cursor, conn

def delete_usuario(usuario_id):
    cursor = get_cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (usuario_id,))
    conn.commit()
    cursor.close()
    print("El usuario se ha eliminado correctamente.")
