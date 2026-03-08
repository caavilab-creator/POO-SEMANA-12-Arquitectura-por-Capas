class Usuario:
    """
    Entidad Usuario (modelo).
    Representa un usuario registrado en la biblioteca digital.
    """
    
    def __init__(self, id_usuario: str, nombre: str):
        """
        Inicializa un nuevo usuario.
        
        Args:
            id_usuario: Identificador único del usuario.
            nombre: Nombre completo del usuario.
        """
        self.__id_usuario = id_usuario.strip()
        self.__nombre = nombre.strip()
        self.__libros_prestados = []  # Lista mutable para libros prestados
    
    @property
    def id_usuario(self) -> str:
        """Retorna el ID único del usuario."""
        return self.__id_usuario
    
    @property
    def nombre(self) -> str:
        """Retorna el nombre del usuario."""
        return self.__nombre
    
    @property
    def libros_prestados(self) -> list:
        """
        Retorna la lista de libros actualmente prestados.
        
        Returns:
            Lista con los objetos Libro prestados al usuario.
        """
        return self.__libros_prestados
    
    def agregar_libro_prestado(self, libro) -> bool:
        """
        Agrega un libro a la lista de prestados.
        
        Args:
            libro: Objeto Libro a agregar.
            
        Returns:
            True si se agregó correctamente, False si ya existe.
        """
        if libro not in self.__libros_prestados:
            self.__libros_prestados.append(libro)
            return True
        return False
    
    def remover_libro_prestado(self, libro) -> bool:
        """
        Remueve un libro de la lista de prestados.
        
        Args:
            libro: Objeto Libro a remover.
            
        Returns:
            True si se removió correctamente, False si no existe.
        """
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)
            return True
        return False
    
    def __repr__(self) -> str:
        """Representación en string del objeto Usuario."""
        return f"Usuario(id={self.id_usuario}, nombre={self.nombre}, libros_prestados={len(self.__libros_prestados)})"
    
    def __eq__(self, other) -> bool:
        """
        Compara dos usuarios por su ID (identificador único).
        
        Args:
            other: Otro objeto Usuario para comparar.
            
        Returns:
            True si los IDs coinciden, False en caso contrario.
        """
        if not isinstance(other, Usuario):
            return False
        return self.__id_usuario == other.__id_usuario
    
    def __hash__(self) -> int:
        """
        Genera el hash basado en el ID para permitir uso en colecciones.
        
        Returns:
            Hash del ID de usuario.
        """
        return hash(self.__id_usuario)