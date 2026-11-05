import json
import mysql.connector

with open("config.json", "r") as f:
    config = json.load(f)

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")

print(f"{'ID':<4} {'MARCA':<15} {'MODELO':<12} {'COLOR':<10} {'KM':<8} {'PRECIO':<10}")
print("-" * 65)

for (id_c, marca, modelo, color, km, precio) in cursor.fetchall():
    print(f"{id_c:<4} {marca:<15} {modelo:<12} {color:<10} {km:<8} {precio:<10.2f}")

cursor.close()
conn.close()
