import json

def agregar_receta(nombre, ingredientes, pasos):
    receta = {
        "nombre": nombre,
        "ingredientes": ingredientes,
        "pasos": pasos,
    }
    # Almacenar la receta como un JSON en KeyDB
    client.set(nombre, json.dumps(receta))
    return f"Receta '{nombre}' agregada exitosamente."
