from Negocio import Negocio
from Producto import Producto

limon = Producto('10010','Limon', 'Frutas', 0.8)
plato = Producto('20010', 'Plato', 'Vajilla', 2.4)

negocio = Negocio(productos=[limon, plato])

print('MOSTRAR PRODUCTO'.center(50, '-'))
print(negocio.mostrar_producto('10010'))
print(negocio.mostrar_producto('20010'))

print('ELIMINAR PRODUCTO'.center(50, '-'))
print(negocio.eliminar_producto('10010'))