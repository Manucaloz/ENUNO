import mysql.connector

class Database:
    """
    Clase para manejar la conexión y operaciones con una base de datos MySQL.

    Atributos:
        conn: Conexión a la base de datos.
        cursor: Cursor para ejecutar consultas y recuperar resultados.

    Métodos:
        __init__(self, host, user, password, database):
            Inicializa la conexión a la base de datos con los parámetros proporcionados.

        execute(self, query, params=None):
            Ejecuta una consulta SQL con los parámetros opcionales y confirma los cambios.

        fetchall(self):
            Devuelve todos los resultados de la consulta ejecutada.

        fetchone(self):
            Devuelve un solo resultado de la consulta ejecutada.

        close(self):
            Cierra el cursor y la conexión a la base de datos, manejando errores si es necesario.
    """

    def __init__(self, host, user, password, database):
        """Inicializa la conexión a la base de datos con los parámetros proporcionados."""
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        print("Conectado a la base de datos con éxito")

    def execute(self, query, params=None):
        """Ejecuta una consulta SQL con parámetros opcionales y confirma los cambios."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self):
        """Devuelve todos los resultados de la consulta ejecutada."""
        return self.cursor.fetchall()

    def fetchone(self):
        """Devuelve un solo resultado de la consulta ejecutada."""
        return self.cursor.fetchone()

    def close(self):
        """Cierra el cursor y la conexión a la base de datos, manejando errores si es necesario."""
        try:
            while self.cursor.nextset():
                pass
        except mysql.connector.errors.InterfaceError:
            pass
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = Database(host='127.0.0.1', user='root', password='12345678', database='enuno')
    db.close()
