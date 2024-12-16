from flask import Flask, render_template, request, redirect, url_for
import redis
import json

app = Flask(__name__)

# Conexión a KeyDB (Redis)
keydb = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Funciones auxiliares para manejar datos en KeyDB
def obtener_articulos():
    articulos = []
    for key in keydb.keys("articulo:*"):
        articulos.append(json.loads(keydb.get(key)))
    return articulos

def guardar_articulo(articulo):
    keydb.set(f"articulo:{articulo['id']}", json.dumps(articulo))

def eliminar_articulo_por_id(id_articulo):
    keydb.delete(f"articulo:{id_articulo}")

def obtener_articulo_por_id(id_articulo):
    articulo_json = keydb.get(f"articulo:{id_articulo}")
    return json.loads(articulo_json) if articulo_json else None

# Ruta principal que lista todos los artículos
@app.route('/')
def index():
    articulos = obtener_articulos()
    return render_template('index.html', articulos=articulos)

# Ruta para agregar un artículo
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = float(request.form['cantidad'])
        precio = float(request.form['precio'])
        nuevo_id = keydb.incr('id_articulo')  # Generar un nuevo ID
        articulo = {
            'id': nuevo_id,
            'nombre': nombre,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio
        }
        guardar_articulo(articulo)
        return redirect(url_for('index'))
    return render_template('agregar.html')

# Ruta para editar un artículo
@app.route('/editar/<int:id_articulo>', methods=['GET', 'POST'])
def editar(id_articulo):
    articulo = obtener_articulo_por_id(id_articulo)
    if not articulo:
        return redirect(url_for('index'))

    if request.method == 'POST':
        articulo['nombre'] = request.form['nombre']
        articulo['descripcion'] = request.form['descripcion']
        articulo['cantidad'] = float(request.form['cantidad'])
        articulo['precio'] = float(request.form['precio'])
        guardar_articulo(articulo)
        return redirect(url_for('index'))

    return render_template('editar.html', articulo=articulo)

# Ruta para eliminar un artículo
@app.route('/eliminar/<int:id_articulo>', methods=['POST'])
def eliminar(id_articulo):
    eliminar_articulo_por_id(id_articulo)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)