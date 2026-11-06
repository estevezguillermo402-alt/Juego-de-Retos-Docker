from pymongo import MongoClient
from prettytable import PrettyTable

# Conexión a MongoDB usando las credenciales y el nombre del contenedor
client = MongoClient("mongodb://mongoadmin:mongopass@mongo-server:27017/?authSource=admin")
db = client["concesionario"]
coleccion = db["coches"]

# Configurar tabla con PrettyTable
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]

# Obtener documentos ordenados por ID
for coche in coleccion.find().sort("id", 1):
    tabla.add_row([
        coche.get("id"),
        coche.get("marca"),
        coche.get("modelo"),
        coche.get("color"),
        coche.get("km"),
        f"{coche.get('precio'):.2f}"
    ])

print(tabla)
client.close()
