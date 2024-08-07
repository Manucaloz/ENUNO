class Model:
    """
    Clase base para modelos ORM.

    Atributos:
        table_name (str): Nombre de la tabla en la base de datos.
        db: Instancia de la clase Database.

    Métodos de clase:
        set_db(cls, db_instance): Asigna una instancia de base de datos.
        create_table(cls): Método abstracto para crear la tabla.
        all(cls): Devuelve todas las instancias del modelo.
        get(cls, **kwargs): Devuelve una instancia del modelo que coincide con los criterios.

    Métodos de instancia:
        save(self): Método abstracto para guardar la instancia.
        delete(self): Elimina la instancia de la base de datos.
    """
    table_name = ''
    db = None

    @classmethod
    def set_db(cls, db_instance):
        """Asigna una instancia de base de datos al modelo."""
        cls.db = db_instance

    @classmethod
    def create_table(cls):
        """Crea la tabla en la base de datos. Debe ser implementado por subclases."""
        raise NotImplementedError

    @classmethod
    def all(cls):
        """Devuelve todas las instancias del modelo desde la base de datos."""
        query = f"SELECT * FROM {cls.table_name}"
        cls.db.execute(query)
        results = cls.db.fetchall()
        return [cls(**result) for result in results]

    @classmethod
    def get(cls, **kwargs):
        """
        Devuelve una instancia que coincide con los criterios dados.

        Args:
            **kwargs: Criterios de búsqueda.

        Returns:
            instance: Instancia del modelo o None si no se encuentra.
        """
        keys = list(kwargs.keys())
        values = tuple(kwargs.values())
        query = f"SELECT * FROM {cls.table_name} WHERE {' AND '.join([f'{key}=%s' for key in keys])}"
        cls.db.execute(query, values)
        result = cls.db.fetchone()
        return cls(**result) if result else None

    def save(self):
        """Guarda la instancia en la base de datos. Debe ser implementado por subclases."""
        raise NotImplementedError

    def delete(self):
        """Elimina la instancia de la base de datos."""
        if self.id is not None:
            query = f"DELETE FROM {self.table_name} WHERE id=%s"
            self.db.execute(query, (self.id,))
            self.id = None
