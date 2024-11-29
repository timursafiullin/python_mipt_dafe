import array
from typing import Iterable

class VectorND:
    _components: array

    def __init__(self, components: Iterable):
        self._components = array.array('d', components)

        if len(self._components) == 0:
            raise ValueError("Vector components cannot be empty")

    def __str__(self):
        string = ", ".join(str(i) for i in self._components)
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
        # Если индекс больше длины вектора, исключение возбуждается объектом 'array'
        if isinstance(key, int) and key >= 1:
            return self._components[key - 1]

    def __eq__(self, other: 'VectorND') -> bool:
        if isinstance(other, VectorND):
            # vector1 - вектор наибольшей размерности, vector2 - наименьшей
            vector1 = self if len(self) >= len(other) else other
            vector2 = other if len(self) >= len(other) else self

            for i in range(len(vector1) - len(vector2)):
                vector2._components.append(0)

            return vector1._components == vector2._components
        else:
            raise TypeError("Invalid argument type. Both arguments should be VectorND objects")

    def __lt__(self, other: 'VectorND') -> bool:
        pass

vec1 = VectorND([1, 2, 3, 0, 0, 1])
vec2 = VectorND([1, 2, 3, 0, 0, 1])

print(vec1 != vec2)

