from conn import get_cursor, conn


def create_table():
    cursor = get_cursor()

    cursor.execute('''DROP TABLE IF EXISTS usuarios''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            email VARCHAR(100),
            descripcion VARCHAR(50),
            sueldo NUMERIC
        )
    ''')

    conn.commit()
    cursor.close()
    print("La tabla de usuarios ha sido creada.")


if __name__ == "__main__":
    create_table()