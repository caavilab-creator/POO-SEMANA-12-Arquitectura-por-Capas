class Libro:
    """
    Entidad Libro (modelo).
    Representa un libro dentro del sistema de biblioteca digital.
    """
    
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        """
        Inicializa un nuevo libro.
        
        Args:
            titulo: Título del libro.
            autor: Autor del libro.
            categoria: Categoría del libro.
            isbn: Identificador único del libro (ISBN).
        """
        # Tupla inmutable para título y autor (requisito técnico)
        self.__informacion = (titulo.strip(), autor.strip())
        self.__categoria = categoria.strip()
        self.__isbn = isbn.strip()
    
    @property
    def titulo(self) -> str:
        """Retorna el título del libro."""
        return self.__informacion[0]
    
    @property
    def autor(self) -> str:
        """Retorna el autor del libro."""
        return self.__informacion[1]
    
    @property
    def informacion(self) -> tuple:
        """Retorna la tupla con título y autor (inmutable)."""
        return self.__informacion
    
    @property
    def categoria(self) -> str:
        """Retorna la categoría del libro."""
        return self.__categoria
    
    @property
    def isbn(self) -> str:
        """Retorna el ISBN del libro."""
        return self.__isbn
    
    def __repr__(self) -> str:
        """Representación en string del objeto Libro."""
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"
    
    def __eq__(self, other) -> bool:
        """
        Compara dos libros por su ISBN (identificador único).
        
        Args:
            other: Otro objeto Libro para comparar.
            
        Returns:
            True si los ISBN coinciden, False en caso contrario.
        """
        if not isinstance(other, Libro):
            return False
        return self.__isbn == other.__isbn
    
    def __hash__(self) -> int:
        """
        Genera el hash basado en el ISBN para permitir uso en colecciones.
        
        Returns:
            Hash del ISBN.
        """
        return hash(self.__isbn)