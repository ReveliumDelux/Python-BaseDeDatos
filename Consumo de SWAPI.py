import requests

def obtener_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def planetas_aridos():
    url = "https://swapi.dev/api/planets/"
    planetas_aridos_count = 0
    while url:
        data = obtener_datos(url)
        if data:
            for planeta in data['results']:
                if "árido" in planeta['climate'].lower():
                    for film_url in planeta['films']:
                        film_data = obtener_datos(film_url)
                        if film_data:
                            planetas_aridos_count += 1
            url = data['next']
        else:
            break
    return planetas_aridos_count

def contar_wookies():
    url = "https://swapi.dev/api/people/"
    wookies_count = 0
    while url:
        data = obtener_datos(url)
        if data:
            for persona in data['results']:
                if "wookie" in persona['species'][0].lower():
                    wookies_count += 1
            url = data['next']
        else:
            break
    return wookies_count

def aeronave_mas_pequena():
    url = "https://swapi.dev/api/starships/"
    smallest_starship = None
    smallest_length = float('inf')
    while url:
        data = obtener_datos(url)
        if data:
            for starship in data['results']:
                if "1" in starship['films']:
                    length = starship['length']
                    if length != "unknown" and float(length) < smallest_length:
                        smallest_length = float(length)
                        smallest_starship = starship['name']
            url = data['next']
        else:
            break
    return smallest_starship

print("a) Planetas con clima árido en películas:", planetas_aridos())
print("b) Número de Wookies en la saga:", contar_wookies())
print("c) Nombre de la aeronave más pequeña en la primera película:", aeronave_mas_pequena())