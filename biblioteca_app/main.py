"""
Punto de entrada principal del Sistema de Gestión de Biblioteca Digital.
Contiene únicamente la interfaz de usuario (menú en consola).
NO contiene lógica de negocio.
"""

from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu() -> None:
    """Muestra el menú principal de opciones."""
    print("\n" + "=" * 50)
    print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
    print("=" * 50)
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados a usuario")
    print("9. Mostrar todos los libros")
    print("10. Mostrar todos los usuarios")
    print("0. Salir")
    print("=" * 50)


def opcion_anadir_libro(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de añadir un nuevo libro."""
    print("\n--- AÑADIR LIBRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    isbn = input("ISBN: ")
    
    resultado = servicio.anadir_libro(titulo, autor, categoria, isbn)
    print("✅ Libro añadido correctamente." if resultado else "❌ Error: No se pudo añadir el libro (posible ISBN duplicado).")


def opcion_quitar_libro(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de quitar un libro."""
    print("\n--- QUITAR LIBRO ---")
    isbn = input("ISBN del libro a quitar: ")
    
    resultado = servicio.quitar_libro(isbn)
    print("✅ Libro quitado correctamente." if resultado else "❌ Error: Libro no encontrado.")


def opcion_registrar_usuario(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de registrar un nuevo usuario."""
    print("\n--- REGISTRAR USUARIO ---")
    id_usuario = input("ID de usuario: ")
    nombre = input("Nombre completo: ")
    
    resultado = servicio.registrar_usuario(id_usuario, nombre)
    print("✅ Usuario registrado correctamente." if resultado else "❌ Error: No se pudo registrar el usuario (posible ID duplicado).")


def opcion_dar_baja_usuario(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de dar de baja un usuario."""
    print("\n--- DAR DE BAJA USUARIO ---")
    id_usuario = input("ID de usuario: ")
    
    resultado = servicio.dar_baja_usuario(id_usuario)
    print("✅ Usuario dado de baja correctamente." if resultado else "❌ Error: Usuario no encontrado o tiene libros prestados.")


def opcion_prestar_libro(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de prestar un libro."""
    print("\n--- PRESTAR LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")
    
    resultado = servicio.prestar_libro(isbn, id_usuario)
    if resultado == 0:
        print("✅ Préstamo realizado correctamente.")
    elif resultado == 1:
        print("❌ Error: Libro no encontrado.")
    elif resultado == 2:
        print("❌ Error: Usuario no encontrado.")
    elif resultado == 3:
        print("❌ Error: Libro ya está prestado.")
    elif resultado == 4:
        print("❌ Error: Usuario ya tiene este libro prestado.")


def opcion_devolver_libro(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de devolver un libro."""
    print("\n--- DEVOLVER LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")
    
    resultado = servicio.devolver_libro(isbn, id_usuario)
    if resultado == 0:
        print("✅ Devolución realizada correctamente.")
    elif resultado == 1:
        print("❌ Error: Libro no encontrado.")
    elif resultado == 2:
        print("❌ Error: Usuario no encontrado.")
    elif resultado == 3:
        print("❌ Error: El usuario no tiene este libro prestado.")


def opcion_buscar_libros(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de buscar libros."""
    print("\n--- BUSCAR LIBROS ---")
    print("1. Por título")
    print("2. Por autor")
    print("3. Por categoría")
    opcion = input("Seleccione opción: ")
    
    criterio = input("Ingrese el criterio de búsqueda: ")
    resultados = []
    
    if opcion == "1":
        resultados = servicio.buscar_por_titulo(criterio)
    elif opcion == "2":
        resultados = servicio.buscar_por_autor(criterio)
    elif opcion == "3":
        resultados = servicio.buscar_por_categoria(criterio)
    else:
        print("❌ Opción no válida.")
        return
    
    if resultados:
        print(f"\n📖 Se encontraron {len(resultados)} libro(s):")
        for libro in resultados:
            print(f"  - {libro}")
    else:
        print("📭 No se encontraron libros con ese criterio.")


def opcion_listar_prestados(servicio: BibliotecaServicio) -> None:
    """Gestiona la opción de listar libros prestados a un usuario."""
    print("\n--- LISTAR LIBROS PRESTADOS ---")
    id_usuario = input("ID del usuario: ")
    
    resultados = servicio.listar_libros_prestados(id_usuario)
    
    if resultados is not None:
        if resultados:
            print(f"\n📚 Libros prestados a {resultados[0].nombre if resultados else 'usuario'}:")
            for libro in resultados:
                print(f"  - {libro}")
        else:
            print("📭 El usuario no tiene libros prestados.")
    else:
        print("❌ Error: Usuario no encontrado.")


def opcion_mostrar_todos_libros(servicio: BibliotecaServicio) -> None:
    """Muestra todos los libros disponibles."""
    print("\n--- CATÁLOGO COMPLETO ---")
    libros = servicio.obtener_todos_los_libros()
    
    if libros:
        print(f"\n📖 Total: {len(libros)} libro(s) en catálogo:")
        for libro in libros:
            print(f"  - {libro}")
    else:
        print("📭 No hay libros en el catálogo.")


def opcion_mostrar_todos_usuarios(servicio: BibliotecaServicio) -> None:
    """Muestra todos los usuarios registrados."""
    print("\n--- USUARIOS REGISTRADOS ---")
    usuarios = servicio.obtener_todos_los_usuarios()
    
    if usuarios:
        print(f"\n👥 Total: {len(usuarios)} usuario(s) registrados:")
        for usuario in usuarios:
            print(f"  - {usuario}")
    else:
        print("📭 No hay usuarios registrados.")


def main() -> None:
    """
    Función principal del programa.
    Inicializa el servicio y ejecuta el menú interactivo.
    """
    servicio = BibliotecaServicio()
    
    print("\n🎉 ¡Bienvenido al Sistema de Biblioteca Digital!")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            opcion_anadir_libro(servicio)
        elif opcion == "2":
            opcion_quitar_libro(servicio)
        elif opcion == "3":
            opcion_registrar_usuario(servicio)
        elif opcion == "4":
            opcion_dar_baja_usuario(servicio)
        elif opcion == "5":
            opcion_prestar_libro(servicio)
        elif opcion == "6":
            opcion_devolver_libro(servicio)
        elif opcion == "7":
            opcion_buscar_libros(servicio)
        elif opcion == "8":
            opcion_listar_prestados(servicio)
        elif opcion == "9":
            opcion_mostrar_todos_libros(servicio)
        elif opcion == "10":
            opcion_mostrar_todos_usuarios(servicio)
        elif opcion == "0":
            print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()