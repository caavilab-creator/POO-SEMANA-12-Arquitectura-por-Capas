from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Capa de servicio: lógica de negocio del sistema de biblioteca.
    - libros: dict (ISBN -> Libro)
    - usuarios: dict (ID usuario -> Usuario)
    - ids_usuarios: set para unicidad de IDs
    """
    
    def __init__(self):
        """Inicializa el servicio con las colecciones vacías."""
        self.libros: dict[str, Libro] = {}
        self.usuarios: dict[str, Usuario] = {}
        self.ids_usuarios: set[str] = set()
    
    # =======================
    # GESTIÓN DE LIBROS
    # =======================
    
    def anadir_libro(self, titulo: str, autor: str, categoria: str, isbn: str) -> bool:
        """
        Añade un nuevo libro al catálogo.
        
        Args:
            titulo: Título del libro.
            autor: Autor del libro.
            categoria: Categoría del libro.
            isbn: Identificador único del libro.
            
        Returns:
            True si se añadió correctamente, False si ya existe.
        """
        titulo = (titulo or "").strip()
        autor = (autor or "").strip()
        categoria = (categoria or "").strip()
        isbn = (isbn or "").strip()
        
        if not titulo or not autor or not isbn:
            raise ValueError("Título, autor e ISBN son obligatorios.")
        
        if isbn in self.libros:
            return False  # ISBN duplicado
        
        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro
        return True
    
    def quitar_libro(self, isbn: str) -> bool:
        """
        Elimina un libro del catálogo.
        
        Args:
            isbn: ISBN del libro a eliminar.
            
        Returns:
            True si se eliminó correctamente, False si no existe.
        """
        isbn = (isbn or "").strip()
        
        if isbn not in self.libros:
            return False  # Libro no encontrado
        
        # Validar: no eliminar si está prestado
        for usuario in self.usuarios.values():
            for libro_prestado in usuario.libros_prestados:
                if libro_prestado.isbn == isbn:
                    return False  # Libro está prestado
        
        del self.libros[isbn]
        return True
    
    def obtener_todos_los_libros(self) -> list[Libro]:
        """
        Retorna todos los libros del catálogo.
        
        Returns:
            Lista con todos los objetos Libro.
        """
        return list(self.libros.values())
    
    # =======================
    # GESTIÓN DE USUARIOS
    # =======================
    
    def registrar_usuario(self, id_usuario: str, nombre: str) -> bool:
        """
        Registra un nuevo usuario en el sistema.
        
        Args:
            id_usuario: Identificador único del usuario.
            nombre: Nombre completo del usuario.
            
        Returns:
            True si se registró correctamente, False si ya existe.
        """
        id_usuario = (id_usuario or "").strip()
        nombre = (nombre or "").strip()
        
        if not id_usuario or not nombre:
            raise ValueError("ID y nombre del usuario son obligatorios.")
        
        if id_usuario in self.ids_usuarios:
            return False  # ID duplicado
        
        usuario = Usuario(id_usuario, nombre)
        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)
        return True
    
    def dar_baja_usuario(self, id_usuario: str) -> bool:
        """
        Da de baja un usuario del sistema.
        
        Args:
            id_usuario: ID del usuario a eliminar.
            
        Returns:
            True si se eliminó correctamente, False si no existe o tiene libros prestados.
        """
        id_usuario = (id_usuario or "").strip()
        
        if id_usuario not in self.usuarios:
            return False  # Usuario no encontrado
        
        usuario = self.usuarios[id_usuario]
        
        # Validar: no eliminar si tiene libros prestados
        if usuario.libros_prestados:
            return False  # Tiene libros prestados
        
        del self.usuarios[id_usuario]
        self.ids_usuarios.discard(id_usuario)
        return True
    
    def obtener_todos_los_usuarios(self) -> list[Usuario]:
        """
        Retorna todos los usuarios registrados.
        
        Returns:
            Lista con todos los objetos Usuario.
        """
        return list(self.usuarios.values())
    
    # =======================
    # PRÉSTAMOS Y DEVOLUCIONES
    # =======================
    
    def prestar_libro(self, isbn: str, id_usuario: str) -> int:
        """
        Realiza el préstamo de un libro a un usuario.
        
        Args:
            isbn: ISBN del libro a prestar.
            id_usuario: ID del usuario que recibe el préstamo.
            
        Returns:
            0: Éxito
            1: Libro no encontrado
            2: Usuario no encontrado
            3: Libro ya está prestado
            4: Usuario ya tiene este libro prestado
        """
        isbn = (isbn or "").strip()
        id_usuario = (id_usuario or "").strip()
        
        # Validar existencia del libro
        if isbn not in self.libros:
            return 1
        
        # Validar existencia del usuario
        if id_usuario not in self.usuarios:
            return 2
        
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        
        # Validar: libro ya está prestado (está en la lista de algún usuario)
        for usr in self.usuarios.values():
            for libro_prestado in usr.libros_prestados:
                if libro_prestado.isbn == isbn:
                    return 3  # Libro ya prestado
        
        # Validar: usuario ya tiene este libro (caso edge)
        if libro in usuario.libros_prestados:
            return 4
        
        # Realizar préstamo
        usuario.agregar_libro_prestado(libro)
        return 0
    
    def devolver_libro(self, isbn: str, id_usuario: str) -> int:
        """
        Realiza la devolución de un libro por un usuario.
        
        Args:
            isbn: ISBN del libro a devolver.
            id_usuario: ID del usuario que devuelve el libro.
            
        Returns:
            0: Éxito
            1: Libro no encontrado
            2: Usuario no encontrado
            3: El usuario no tiene este libro prestado
        """
        isbn = (isbn or "").strip()
        id_usuario = (id_usuario or "").strip()
        
        # Validar existencia del libro
        if isbn not in self.libros:
            return 1
        
        # Validar existencia del usuario
        if id_usuario not in self.usuarios:
            return 2
        
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        
        # Validar: usuario tiene el libro prestado
        if libro not in usuario.libros_prestados:
            return 3
        
        # Realizar devolución
        usuario.remover_libro_prestado(libro)
        return 0
    
    # =======================
    # BÚSQUEDAS
    # =======================
    
    def buscar_por_titulo(self, criterio: str) -> list[Libro]:
        """
        Busca libros por título (búsqueda parcial, case-insensitive).
        
        Args:
            criterio: Texto a buscar en el título.
            
        Returns:
            Lista de libros que coinciden con el criterio.
        """
        criterio = (criterio or "").strip().lower()
        resultados = []
        
        for libro in self.libros.values():
            if criterio in libro.titulo.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_autor(self, criterio: str) -> list[Libro]:
        """
        Busca libros por autor (búsqueda parcial, case-insensitive).
        
        Args:
            criterio: Texto a buscar en el autor.
            
        Returns:
            Lista de libros que coinciden con el criterio.
        """
        criterio = (criterio or "").strip().lower()
        resultados = []
        
        for libro in self.libros.values():
            if criterio in libro.autor.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_categoria(self, criterio: str) -> list[Libro]:
        """
        Busca libros por categoría (búsqueda parcial, case-insensitive).
        
        Args:
            criterio: Texto a buscar en la categoría.
            
        Returns:
            Lista de libros que coinciden con el criterio.
        """
        criterio = (criterio or "").strip().lower()
        resultados = []
        
        for libro in self.libros.values():
            if criterio in libro.categoria.lower():
                resultados.append(libro)
        
        return resultados
    
    def listar_libros_prestados(self, id_usuario: str) -> list[Usuario] | None:
        """
        Lista los libros actualmente prestados a un usuario.
        
        Args:
            id_usuario: ID del usuario a consultar.
            
        Returns:
            Lista de libros prestados, o None si el usuario no existe.
        """
        id_usuario = (id_usuario or "").strip()
        
        if id_usuario not in self.usuarios:
            return None  # Usuario no encontrado
        
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados