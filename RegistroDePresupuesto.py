import sqlite3

def conectar_base_datos():
    conexion = sqlite3.connect("presupuesto.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articulos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        cantidad REAL NOT NULL,
                        precio REAL NOT NULL
                      )''')
    conexion.commit()
    return conexion, cursor

def agregar_articulo(nombre, cantidad, precio):
    cursor.execute("INSERT INTO articulos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                   (nombre, cantidad, precio))
    conexion.commit()
    print(f"\nArtículo '{nombre}' agregado exitosamente.\n")

def listar_articulos():
    cursor.execute("SELECT * FROM articulos")
    articulos = cursor.fetchall()
    if articulos:
        print("\n--- Lista de artículos ---")
        for articulo in articulos:
            print(f"ID: {articulo[0]}, Nombre: {articulo[1]}, Cantidad: {articulo[2]}, Precio: ${articulo[3]:.2f}")
    else:
        print("\nNo hay artículos registrados.\n")

def eliminar_articulo(id_articulo):
    cursor.execute("DELETE FROM articulos WHERE id = ?", (id_articulo,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"\nArtículo con ID {id_articulo} eliminado exitosamente.\n")
    else:
        print(f"\nNo se encontró un artículo con ID {id_articulo}.\n")

def menu():
    while True:
        print("\n--- Sistema de Registro de Presupuesto ---")
        print("1. Agregar artículo")
        print("2. Listar artículos")
        print("3. Eliminar artículo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del artículo: ")
            cantidad = float(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_articulo(nombre, cantidad, precio)

        elif opcion == "2":
            listar_articulos()

        elif opcion == "3":
            id_articulo = int(input("Ingrese el ID del artículo a eliminar: "))
            eliminar_articulo(id_articulo)

        elif opcion == "4":
            print("\nSaliendo del sistema...\n")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    conexion, cursor = conectar_base_datos()
    try:
        menu()
    finally:
        conexion.close()
