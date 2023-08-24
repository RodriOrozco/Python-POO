class Producto:
    def __init__(self, cod, nombre, categoria, pvp):
        self._cod = cod
        self._nombre = nombre
        self._categoria = categoria
        self._pvp = pvp

    def __str__(self):
        return '{} {}'.format(self._nombre, self._pvp)