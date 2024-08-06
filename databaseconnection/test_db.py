from connection import Database

def test_db_operations():
    try:
        # Conectar a la base de datos
        db = Database(host='127.0.0.1', user='root', password='12345678', database='enuno')
        
        # Crear la tabla si no existe
        db.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        
        # Insertar un registro
        db.execute("INSERT INTO test_table (name) VALUES (%s)", ("Test Name",))
        
        # Realizar una sola consulta
        db.execute("SELECT * FROM test_table")
        
        # Obtener y mostrar los resultados
        results = db.fetchall()
        for row in results:
            print(row)
        
        # Cerrar la conexión a la base de datos
        db.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_db_operations()
