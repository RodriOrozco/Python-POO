class Negocio:
    def __init__(self, productos=[]):
        self._productos = productos

    def mostrar_producto(self, cod=None):
        for producto in self._productos:
            if producto._cod == cod:
                return f'{producto}'
        print('Producto no encontrado')

    def eliminar_producto(self, cod=None):
        for i, producto in enumerate(self._productos):
            if producto._cod == cod:
                del(self._productos[i])
                return f'{producto} -> ELIMINADO'

        print('Producto no encontrado')