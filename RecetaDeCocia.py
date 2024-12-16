import sqlite3

def conectar_bd():
    return sqlite3.connect("recetas.db")

def crear_tabla():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS recetas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        ingredientes TEXT NOT NULL,
                        pasos TEXT NOT NULL)''')
    conexion.commit()
    conexion.close()

def agregar_receta():
    nombre = input("Ingresa el nombre de la receta: ")
    ingredientes = input("Ingresa los ingredientes (separados por comas): ")
    pasos = input("Ingresa los pasos para preparar la receta: ")

    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)",
                   (nombre, ingredientes, pasos))
    conexion.commit()
    conexion.close()
    print("\nReceta agregada exitosamente!\n")

def actualizar_receta():
    id_receta = input("Ingresa el ID de la receta a actualizar: ")
    nombre = input("Nuevo nombre de la receta (o presiona Enter para no cambiar): ")
    ingredientes = input("Nuevos ingredientes (o presiona Enter para no cambiar): ")
    pasos = input("Nuevos pasos (o presiona Enter para no cambiar): ")

    conexion = conectar_bd()
    cursor = conexion.cursor()

    if nombre:
        cursor.execute("UPDATE recetas SET nombre = ? WHERE id = ?", (nombre, id_receta))
    if ingredientes:
        cursor.execute("UPDATE recetas SET ingredientes = ? WHERE id = ?", (ingredientes, id_receta))
    if pasos:
        cursor.execute("UPDATE recetas SET pasos = ? WHERE id = ?", (pasos, id_receta))

    conexion.commit()
    conexion.close()
    print("\nReceta actualizada exitosamente!\n")

def eliminar_receta():
    id_receta = input("Ingresa el ID de la receta a eliminar: ")

    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM recetas WHERE id = ?", (id_receta,))
    conexion.commit()
    conexion.close()
    print("\nReceta eliminada exitosamente!\n")

def listar_recetas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()
    conexion.close()

    if recetas:
        print("\nListado de recetas:")
        for receta in recetas:
            print(f"ID: {receta[0]}, Nombre: {receta[1]}")
    else:
        print("\nNo hay recetas registradas.\n")

def buscar_receta():
    id_receta = input("Ingresa el ID de la receta que deseas consultar: ")

    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM recetas WHERE id = ?", (id_receta,))
    receta = cursor.fetchone()
    conexion.close()

    if receta:
        print("\nDetalles de la receta:")
        print(f"Nombre: {receta[1]}")
        print(f"Ingredientes: {receta[2]}")
        print(f"Pasos: {receta[3]}\n")
    else:
        print("\nNo se encontró ninguna receta con ese ID.\n")

def menu():
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_receta()
        elif opcion == "2":
            actualizar_receta()
        elif opcion == "3":
            eliminar_receta()
        elif opcion == "4":
            listar_recetas()
        elif opcion == "5":
            buscar_receta()
        elif opcion == "6":
            print("\n¡Gracias por usar el libro de recetas!\n")
            break
        else:
            print("\nOpción no válida, por favor intenta nuevamente.\n")

if __name__ == "__main__":
    crear_tabla()
    menu()
