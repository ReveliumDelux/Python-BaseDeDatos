from database import SessionLocal
from funciones import agregar_receta, obtener_recetas

db = SessionLocal()

# Agregar una receta
agregar_receta(db, "Tacos", "Tortillas, carne, salsa", "1. Cocina la carne. 2. Prepara las tortillas. 3. Arma los tacos.")

# Listar recetas
recetas = obtener_recetas(db)
for receta in recetas:
    print(f"{receta.nombre}: {receta.ingredientes}")
