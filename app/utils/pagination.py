from flask import request, url_for

class Pagination:
    """Clase para manejar la paginación en las vistas"""
    
    def __init__(self, query, page, per_page=10, endpoint=None, **kwargs):
        """
        Inicializa un objeto de paginación
        
        Args:
            query: Query de SQLAlchemy a paginar
            page: Número de página actual
            per_page: Elementos por página
            endpoint: Endpoint de Flask para generar URLs
            **kwargs: Argumentos adicionales para pasar a url_for
        """
        self.query = query
        self.page = page
        self.per_page = per_page
        self.endpoint = endpoint
        self.kwargs = kwargs
        
        # Ejecutar la consulta paginada
        self.items = self.query.limit(per_page).offset((page - 1) * per_page).all()
        
        # Contar el total de elementos sin paginación
        self.total = self.query.count()
        
        # Calcular el total de páginas
        self.pages = (self.total + per_page - 1) // per_page
    
    @property
    def has_prev(self):
        """Verifica si hay página anterior"""
        return self.page > 1
    
    @property
    def has_next(self):
        """Verifica si hay página siguiente"""
        return self.page < self.pages
    
    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        """
        Genera números de página para mostrar en la navegación
        
        Args:
            left_edge: Número de páginas en el borde izquierdo
            left_current: Número de páginas a la izquierda de la página actual
            right_current: Número de páginas a la derecha de la página actual
            right_edge: Número de páginas en el borde derecho
        
        Yields:
            int o None: Número de página o None para indicar un salto
        """
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num
    
    def get_url(self, page):
        """
        Genera la URL para una página específica
        
        Args:
            page: Número de página
            
        Returns:
            str: URL para la página
        """
        if self.endpoint is None:
            return '#'
        
        kwargs = self.kwargs.copy()
        kwargs['page'] = page
        
        # Agregar cualquier otro parámetro de la solicitud actual
        for key, value in request.args.items():
            if key != 'page' and key not in kwargs:
                kwargs[key] = value
        
        return url_for(self.endpoint, **kwargs)