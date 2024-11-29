from typing import Union
from numbers import Real
from math import acos


class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0,
                 ordinate: float = 0):

        if not isinstance(abscissa, Union[float, int]):
            raise TypeError("Abscissa and ordinate must be floats")
        if not isinstance(ordinate, Union[float, int]):
            raise TypeError("Abscissa and ordinate must be floats")

        self._abscissa = abscissa
        self._ordinate = ordinate

    def __str__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only compare Vector2D objects")
        return (self._abscissa == other._abscissa and self._ordinate == other._ordinate)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only compare Vector2D objects")
        return (self._abscissa < other._abscissa) or (self._abscissa == other._abscissa
                                                      and self._ordinate < other._ordinate)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only compare Vector2D objects")
        return self == other or self < other

    def __abs__(self):
        return (self._abscissa**2 + self._ordinate**2)**0.5

    def __bool__(self):
        return (self._abscissa != 0 or self._ordinate != 0)

    def __mul__(self, other: float) -> 'Vector2D':
        if not isinstance(other, Union[int, float]):
            raise TypeError("Can multiply Vector2D by a number")
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __rmul__(self, other: float) -> 'Vector2D':
        if not isinstance(other, Union[int, float]):
            raise TypeError("Can multiply Vector2D by a number")
        return Vector2D(self._abscissa * other, self._ordinate * other)

    def __truediv__(self, other: float) -> 'Vector2D':
        if not isinstance(other, Union[int, float]):
            raise TypeError("Can divide Vector2D by a number")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Vector2D(self._abscissa / other, self._ordinate / other)

    def __add__(self, other) -> 'Vector2D':
        if isinstance(other, Union[int, float]):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        else:
            raise TypeError("Can only add Vector2D objects or numbers to Vector2D objects")

    def __radd__(self, other) -> 'Vector2D':
        if isinstance(other, Union[int, float]):
            return Vector2D(other + self._abscissa, other + self._ordinate)
        elif isinstance(other, Vector2D):
            return Vector2D(other._abscissa + self._abscissa, other._ordinate + self._ordinate)
        else:
            raise TypeError("Can only add Vector2D objects or numbers to Vector2D objects")

    def __sub__(self, other) -> 'Vector2D':
        if isinstance(other, Union[int, float]):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        else:
            raise TypeError("Can only sub Vector2D objects or numbers from Vector2D objects")

    def __neg__(self) -> 'Vector2D':
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return int(abs(self))

    def __matmul__(self, other) -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only supports Vector2D objects")
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    def get_angle(self, other) -> Real:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only get angle with Vector2D objects")
        elif not bool(self) or not bool(other):
            raise ValueError("Cannot get angle with zero vector")
        return acos((self @ other) / (abs(self) * abs(other)))

    # сопряженная
    def __invert__(self) -> 'Vector2D':
        return Vector2D(self._abscissa, -self._ordinate)

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate
