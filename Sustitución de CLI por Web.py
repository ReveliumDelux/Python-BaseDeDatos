from flask import Flask, request, jsonify, render_template
import redis

# Configurar conexión con KeyDB
conexion = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Inicializar Flask
app = Flask(__name__)

# Rutas principales
@app.route('/')
def inicio():
    return render_template('index.html')  # Página principal (crear un archivo index.html si se requiere)

@app.route('/articulos', methods=['GET'])
def listar_articulos():
    """Listar todos los artículos."""
    claves = conexion.keys("articulo:*")
    articulos = [conexion.hgetall(clave) for clave in claves]
    return jsonify(articulos)

@app.route('/articulos', methods=['POST'])
def agregar_articulo():
    """Agregar un nuevo artículo."""
    data = request.json
    if not data.get('nombre') or not data.get('cantidad') or not data.get('precio'):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    id_articulo = conexion.incr("id_articulo")
    clave = f"articulo:{id_articulo}"
    conexion.hset(clave, mapping={
        "id": id_articulo,
        "nombre": data['nombre'],
        "descripcion": data.get('descripcion', ""),
        "cantidad": data['cantidad'],
        "precio": data['precio']
    })
    return jsonify({"mensaje": "Artículo agregado exitosamente", "id": id_articulo})

@app.route('/articulos/<int:id_articulo>', methods=['PUT'])
def editar_articulo(id_articulo):
    """Editar un artículo existente."""
    data = request.json
    clave = f"articulo:{id_articulo}"
    if not conexion.exists(clave):
        return jsonify({"error": "Artículo no encontrado"}), 404

    conexion.hset(clave, mapping={
        "nombre": data.get('nombre', conexion.hget(clave, 'nombre')),
        "descripcion": data.get('descripcion', conexion.hget(clave, 'descripcion')),
        "cantidad": data.get('cantidad', conexion.hget(clave, 'cantidad')),
        "precio": data.get('precio', conexion.hget(clave, 'precio'))
    })
    return jsonify({"mensaje": "Artículo actualizado exitosamente"})

@app.route('/articulos/<int:id_articulo>', methods=['DELETE'])
def eliminar_articulo(id_articulo):
    """Eliminar un artículo."""
    clave = f"articulo:{id_articulo}"
    if conexion.delete(clave):
        return jsonify({"mensaje": "Artículo eliminado exitosamente"})
    return jsonify({"error": "Artículo no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
