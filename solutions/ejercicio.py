"""Ejemplo de creación de dos ficheros JSON: clientes y ventas."""
import json


def crear_fichero_json(nombre_fichero, datos):
    """Crea un fichero JSON con los datos proporcionados."""
    with open(nombre_fichero, "w", encoding="utf-8") as fichero:
        json.dump(datos, fichero, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    clientes = [
        {"cliente_id": 1, "nombre": "Ana", "email": "ana@example.com", "pais": "España"},
        {"cliente_id": 2, "nombre": "Luis", "email": "luis@example.com", "pais": "México"},
        {"cliente_id": 3, "nombre": "María", "email": "maria@example.com", "pais": "Argentina"}
    ]

    ventas = [
        {"venta_id": 101, "cliente_id": 1, "producto": "Laptop", "cantidad": 1, "precio": 1200.0},
        {"venta_id": 102, "cliente_id": 2, "producto": "Móvil", "cantidad": 2, "precio": 450.0},
        {"venta_id": 103, "cliente_id": 1, "producto": "Auriculares", "cantidad": 1, "precio": 75.0}
    ]

    crear_fichero_json("clientes.json", clientes)
    crear_fichero_json("ventas.json", ventas)

    print("Fichero de datos creado: clientes.json")
    print("Fichero de datos creado: ventas.json")
