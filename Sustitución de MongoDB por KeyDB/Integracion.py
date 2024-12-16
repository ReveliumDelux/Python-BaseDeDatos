def menu():
    while True:
        print("\n--- Libro de Recetas con KeyDB ---")
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
            print(agregar_receta(nombre, ingredientes, pasos))
        
        elif opcion == "2":
            recetas = listar_recetas()
            print("\nRecetas disponibles:")
            for receta in recetas:
                print(f"- {receta}")
        
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
            print(actualizar_receta(nombre, nuevos_ingredientes, nuevos_pasos))
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre de la receta a eliminar: ")
            print(eliminar_receta(nombre))
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
b