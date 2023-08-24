import math
class Punto:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Coordenadas: {self._x}, {self._y}'

    def cuadrante(self):
        if self._x > 0 and self._y > 0:
            print(f'{self} pertenece al primer cuadrante')
        elif self._x < 0 and self._y > 0:
            print(f'{self} pertenece al segundo cuadrante')
        elif self._x < 0 and self._y < 0:
            print(f'{self} pertenece al tercer cuadrante')
        elif self._x > 0 and self._y < 0:
            print(f'{self} pertenece al cuarto cuadrante')

        elif self._x != 0 and self._y == 0:
            print(f'{self} se ubica sobre el eje X')
        elif self._x == 0 and self._y != 0:
            print(f'{self} se ubica sobre el eje Y')

        else:
            print(f'{self} se ubica en el origen')

    def vector(self, p):
        print(f'el vector que une los puntos {self} y {p} es igual a ({p._x - self._x}, {p._y - self._y})')
    def distancia(self, p):
        mod = math.sqrt((p._x - self._x) ** 2 + (p._y - self._y) ** 2)
        print(f'La distancia entre los dos puntos {self} y {p} es igual a {mod}')


a = Punto(5, 8)
b = Punto(10, 2)
c = Punto(4, 6)
d = Punto(-8, 4)

print(f'{c}')
d.cuadrante()
a.vector(d)
a.distancia(d)