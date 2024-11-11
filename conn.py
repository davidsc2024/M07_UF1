import psycopg2

conn = psycopg2.connect(
        database="postgres",
        user='dcarbajal',
        password='123',
        host='localhost',
        port='5432'
)

def get_cursor():
    return conn.cursor()