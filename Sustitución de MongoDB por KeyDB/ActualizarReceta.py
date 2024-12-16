def actualizar_receta(nombre, nuevos_ingredientes, nuevos_pasos):
    receta = buscar_receta(nombre)
    if receta:
        receta["ingredientes"] = nuevos_ingredientes
        receta["pasos"] = nuevos_pasos
        client.set(nombre, json.dumps(receta))
        return f"Receta '{nombre}' actualizada exitosamente."
    return f"Receta '{nombre}' no encontrada."
