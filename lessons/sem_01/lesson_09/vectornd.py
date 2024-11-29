import array
from math import sqrt
from typing import Iterable
from itertools import zip_longest

class VectorND:
    _components: array

    def __init__(self, components: Iterable):
        self._components = array.array('d', components)

        if len(self._components) == 0:
            raise ValueError("Vector components cannot be empty")

    def __str__(self):
        string = ", ".join(str(int(i)) if i.is_integer() else str(i) for i in self._components)
        if len(string) <= 10:
            return "VectorND(" + string + ")"
        else:
            return "VectorND(" + string[:10] + "...)"

    def __iter__(self):
        return iter(self._components)
    
    def __len__(self) -> int:
        return len(self._components)

    def __contains__(object: 'VectorND', number: int) -> bool:
        if isinstance(object, VectorND) and isinstance(number, int) and number >= 1:
            return number <= len(object)
        else:
            raise TypeError("Invalid argument type. Vector`s dimension should be more or equal 1.")

    def __getitem__(self, key: int):
        if isinstance(key, int):
            if key < 1:
                raise IndexError("Index should be from 1 to N, where N - count of vector components")
            if key > len(self):
                raise IndexError("Index out of range")
            return self._components[key - 1]

    def __eq__(self, other: 'VectorND') -> bool:
        if isinstance(other, VectorND):
            for elem1, elem2 in zip_longest(self._components, other._components, fillvalue=0):
                if elem1 != elem2:
                    return False
            return True
        else:
            raise TypeError("Invalid argument type. Both arguments should be VectorND objects")

    def __lt__(self, other: 'VectorND') -> bool:
        if isinstance(other, VectorND):
            for elem1, elem2 in zip_longest(self._components, other._components, fillvalue=0):
                if elem1 < elem2:
                    return True
                elif elem1 > elem2:
                    return False
                else:
                    continue
            return False
        else:
            raise TypeError("Invalid argument type. Both arguments should be VectorND objects")

    def __le__(self, other: 'VectorND') -> bool:
        if isinstance(other, VectorND):
            return self.__eq__(other) or self.__lt__(other)
        else:
            raise TypeError("Invalid argument type. Both arguments should be VectorND objects")

    def __abs__(self) -> float:
        return sqrt(sum(component ** 2 for component in self._components))

    def __bool__(self) -> bool:
        return False if abs(self) == 0 else True

    def __mul__(self, number) -> 'VectorND':
        if isinstance(number, (int, float)):
            return VectorND(component * number for component in self._components)
        else:
            raise TypeError("Invalid argument type. Argument should be a number")

    def __rmul__(self, number) -> 'VectorND':
        if isinstance(number, (int, float)):
            return VectorND(component * number for component in self._components)
        else:
            raise TypeError("Invalid argument type. Argument should be a number")

    def __truediv__(self, number) -> 'VectorND':
        if isinstance(number, (int, float)):
            return self * (1 / number)
        else:
            raise TypeError("Invalid argument type. Argument should be a number")

    def __add__(self, other) -> 'VectorND':
        if isinstance(other, VectorND):
            components = array.array("d")
            for c1, c2 in zip_longest(self._components, other._components, fillvalue=0):
                components.append(c1 + c2)
            return VectorND(components)
        if isinstance(other, (int, float)):
            return VectorND(component + other for component in self._components)
        else:
            raise TypeError("Invalid argument type. Arguments should be VectorND or numbers")

    def __radd__(self, other) -> 'VectorND':
        return self.__add__(other)

    def __neg__(self) -> 'VectorND':
        return VectorND(-component for component in self._components)

    def __sub__(self, other) -> 'VectorND':
        if isinstance(other, VectorND):
            components = array.array("d")
            for c1, c2 in zip_longest(self._components, other._components, fillvalue=0):
                components.append(c1 - c2)
            return VectorND(components)
        if isinstance(other, (int, float)):
            return self + (-other)
        else:
            raise TypeError("Invalid argument type. Arguments should be VectorND or numbers")

    def __rsub__(self, other) -> 'VectorND':
        if isinstance(other, (int, float)):
            return -self + other
        else:
            raise TypeError("Invalid argument type. Argument should be a number")

    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return float(abs(self))

    def __matmul__(self, other: 'VectorND') -> float:
        if isinstance(other, VectorND):
            result = sum(a * b for a, b in zip_longest(self._components, other._components, fillvalue=0))
            return result
        else:
            raise TypeError("Invalid argument type. Arguments should be a VectorND")
