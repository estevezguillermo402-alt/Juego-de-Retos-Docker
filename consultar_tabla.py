import json
import mysql.connector
from prettytable import PrettyTable

# Cargar credenciales desde config.json
with open("config.json", "r") as f:
    config = json.load(f)

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")

# Configurar tabla con PrettyTable
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]

for fila in cursor.fetchall():
    tabla.add_row(fila)

print(tabla)

cursor.close()
conn.close()
