def buscar_receta(nombre):
    receta_json = client.get(nombre)
    if receta_json:
        return json.loads(receta_json)
    return None
