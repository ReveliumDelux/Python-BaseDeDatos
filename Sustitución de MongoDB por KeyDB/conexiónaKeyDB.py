import redis

# Configuración de la conexión
REDIS_HOST = "localhost"  # Cambiar si usas KeyDB en un servidor remoto
REDIS_PORT = 6379
REDIS_DB = 0

# Conexión a KeyDB
client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
