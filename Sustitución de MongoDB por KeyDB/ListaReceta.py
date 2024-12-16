def listar_recetas():
    # Obtener todas las claves
    claves = client.keys()
    return [clave for clave in claves]
