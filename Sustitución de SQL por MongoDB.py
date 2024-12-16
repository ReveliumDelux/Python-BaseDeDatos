from funciones import agregar_receta, listar_recetas, buscar_receta, actualizar_receta, eliminar_receta

def menu():
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Ver listado de recetas")
        print("3. Buscar una receta")
        print("4. Actualizar una receta")
        print("5. Eliminar una receta")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la receta: ")
            ingredientes = input("Ingredientes (separados por comas): ")
            pasos = input("Pasos: ")
            agregar_receta(nombre, ingredientes, pasos)
            print("Receta agregada exitosamente.")
        
        elif opcion == "2":
            recetas = listar_recetas()
            print("\nRecetas disponibles:")
            for receta in recetas:
                print(f"- {receta['nombre']}")
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre de la receta: ")
            receta = buscar_receta(nombre)
            if receta:
                print(f"\nNombre: {receta['nombre']}")
                print(f"Ingredientes: {receta['ingredientes']}")
                print(f"Pasos: {receta['pasos']}")
            else:
                print("Receta no encontrada.")
        
        elif opcion == "4":
            nombre = input("Ingrese el nombre de la receta a actualizar: ")
            nuevos_ingredientes = input("Nuevos ingredientes: ")
            nuevos_pasos = input("Nuevos pasos: ")
            if actualizar_receta(nombre, nuevos_ingredientes, nuevos_pasos):
                print("Receta actualizada exitosamente.")
            else:
                print("Error: Receta no encontrada.")
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre de la receta a eliminar: ")
            if eliminar_receta(nombre):
                print("Receta eliminada exitosamente.")
            else:
                print("Error: Receta no encontrada.")
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
