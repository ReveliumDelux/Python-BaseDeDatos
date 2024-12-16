def eliminar_receta(nombre):
    resultado = client.delete(nombre)
    if resultado:
        return f"Receta '{nombre}' eliminada exitosamente."
    return f"Receta '{nombre}' no encontrada."
