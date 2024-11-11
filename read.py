from conn import get_cursor

def read_usuarios():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    cursor.close()
