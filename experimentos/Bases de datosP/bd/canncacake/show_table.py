import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    dbname="cannacake",
    user="postgres",
    password="123"
)
cursor = conexion.cursor()

cursor.execute("SELECT * FROM productos;")
resultados = cursor.fetchall()
print(resultados)