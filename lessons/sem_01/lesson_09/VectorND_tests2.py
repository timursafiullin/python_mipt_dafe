import pytest
from math import isclose

from vectornd import VectorND


# Тесты на инициализацию
def test_initialization():
    # Корректные случаи
    assert VectorND([1, 2, 3])  # Целые числа
    assert VectorND([1.0, 2.0, 3.0])  # Вещественные числа
    assert VectorND(range(10))  # Генератор
    assert VectorND((0, 1, 2))  # Кортеж

    # Некорректные случаи
    with pytest.raises(TypeError):
        VectorND("string")  # Не итерируемое
    with pytest.raises(TypeError):
        VectorND([1, "string", 2])  # Содержит не-число
    with pytest.raises(ValueError):
        VectorND([])  # Пустой список


# Тесты на строковое представление
def test_string_representation():
    assert str(VectorND([1, 2, 3])) == "VectorND(1, 2, 3)"
    assert str(VectorND(range(1000))) == "VectorND(0, 1, 2, 3...)"
    assert str(VectorND(range(1000))) == "VectorND(0, 1, 2, 3...)"
    assert str(VectorND([1.123456789, 2])) == "VectorND(1.12345678...)"  # Обрезка до 10 символов


# Тесты на итерируемость
def test_iteration():
    vector = VectorND([1, 2, 3])
    assert list(vector) == [1, 2, 3]


# Тесты на `len()`
def test_length():
    assert len(VectorND([1, 2, 3])) == 3
    assert len(VectorND(range(100))) == 100


# Тесты на оператор `in`
def test_in_operator():
    vector = VectorND([1, 2, 3])
    assert 1 in vector
    assert 3 in vector
    assert 4 not in vector
    with pytest.raises(TypeError):
        1.5 in vector  # Только целые числа


# Тесты на доступ по индексу
def test_indexing():
    vector = VectorND([1, 2, 3])
    assert vector[1] == 1
    assert vector[3] == 3
    with pytest.raises(IndexError):
        _ = vector[4]
    with pytest.raises(IndexError):
        _ = vector[0]


# Тесты на сравнение векторов (== и !=)
def test_equality():
    assert VectorND([1, 2]) == VectorND([1, 2, 0])
    assert VectorND([1, 2, 3]) != VectorND([1, 2, 4])
    assert VectorND([1, 2]) != VectorND([1, 2, 3])


# Тесты на операции порядка (<, <=, >, >=)
def test_less():
    """ Тесты на < """
    assert VectorND([1, 2]) < VectorND([1, 3])
    assert not VectorND([1, 3]) < VectorND([1, 3])
    assert VectorND([3, 2]) < VectorND([3, 3])
    assert not VectorND([3]) < VectorND([3])

    # 1. Первый меньше по второй компоненте
    assert VectorND([3, 2]) < VectorND([3, 3])

    # 2. Первый меньше по первой компоненте
    assert VectorND([2, 5]) < VectorND([3, 5])

    # 3. Первый меньше по первой компоненте, вторая не сравнивается
    assert VectorND([1, 7]) < VectorND([2, 6])

    # 4. Первый меньше по третьей компоненте, первые две равны
    assert VectorND([4, 5, 6]) < VectorND([4, 5, 7])

    # 5. Первый короче, недостающие компоненты считаются 0
    assert VectorND([1, 2]) < VectorND([1, 2, 3])

    # 6. Первый больше по первой компоненте (не выполняется)
    assert not (VectorND([5, 3]) < VectorND([4, 4]))


    # 8. Первый меньше по второй компоненте, первая равна
    assert VectorND([4, 2]) < VectorND([4, 3])

    # 9. Первый полностью меньше
    assert VectorND([1, 1, 1]) < VectorND([2, 2, 2])

    # 10. Разные длины, второй больше за счет добавления значений
    assert VectorND([1, 2]) < VectorND([1, 2, 1])

    # 1. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 2. Первый вектор равен второму (не меньше)
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 3. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 4. Разные размерности, первый меньше с учетом недостающих нулей
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 5. Разные размерности, первый не меньше с учетом недостающих нулей
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2])
    assert not (v1 < v2)  # False

    # 6. Первый вектор меньше только по одной компоненте
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 7. Первый вектор больше только по последней компоненте
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 8. Все компоненты первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 9. Первый вектор равен нулевому вектору, второй ненулевой
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 1, 1])
    assert v1 < v2  # True

    # 10. Первый вектор имеет одинаковые компоненты, кроме последнего
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True


def test_more():
    """Тесты на > """
    assert VectorND([1, 3]) > VectorND([1, 2])
    assert VectorND([1, 4]) > VectorND([1, 2])
    assert not VectorND([1, 1]) > VectorND([1, 2])
    assert not VectorND([0, 3]) > VectorND([1, 2])

    # 1. Первый больше по второй компоненте
    assert VectorND([3, 4]) > VectorND([3, 3])

    # 2. Первый больше по первой компоненте
    assert VectorND([4, 5]) > VectorND([3, 5])

    # 3. Первый больше по первой компоненте, вторая не сравнивается
    assert VectorND([3, 7]) > VectorND([2, 8])

    # 4. Первый больше по третьей компоненте, первые две равны
    assert VectorND([4, 5, 8]) > VectorND([4, 5, 7])

    # 5. Второй короче, недостающие компоненты считаются 0
    assert VectorND([1, 2, 3]) > VectorND([1, 2])

    # 6. Первый меньше по первой компоненте (не выполняется)
    assert not (VectorND([2, 3]) > VectorND([3, 4]))

    # 8. Первый больше по второй компоненте, первая равна
    assert VectorND([4, 5]) > VectorND([4, 4])

    # 9. Первый полностью больше
    assert VectorND([3, 3, 3]) > VectorND([2, 2, 2])

    # 10. Разные длины, первый больше за счет добавления значений
    assert VectorND([1, 2, 1]) > VectorND([1, 2])


def test_less_or_eq():
    """Тесты на <= """
    assert VectorND([1, 2]) <= VectorND([1, 2])

    # 1. Равные векторы
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 2. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 3. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 <= v2)  # False

    # 4. Разные размерности, вектор меньшей размерности заполняется нулями
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 5. Разные размерности, первый вектор больше с учетом недостающих компонентов
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2])
    assert not (v1 <= v2)  # False

    # 6. Первый вектор равен вектору с нулями в недостающих компонентах
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 <= v2  # True

    # 7. Все элементы первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 8. Первый вектор имеет одинаковые компоненты, кроме одного меньшего
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 9. Первый вектор больше по последнему элементу
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert not (v1 <= v2)  # False

    # 10. Первый вектор равен нулевому вектору
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([0, 0])
    assert v1 <= v2  # True

    # 11 Разные размерности, вектор меньшей размерности имеет нули
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 <= v2  # True

    # 12 Разные размерности, вектор меньшей размерности имеет нули
    v2 = VectorND([1, 2, 0])
    v1 = VectorND([1, 2])
    assert v2 <= v1  # True


def test_more_or_eq():
    """Тесты на >= """
    assert VectorND([1, 3]) >= VectorND([1, 2])
    # 1. Равные векторы
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 2. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 3. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 >= v2)  # False

    # 4. Разные размерности, вектор меньшей размерности имеет нули
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 >= v2  # True

    # 5. Разные размерности, вектор меньшей размерности меньше
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 1])
    assert not (v1 >= v2)  # False

    # 6. Разные размерности, большее значение в меньшем векторе
    v1 = VectorND([1, 3])
    v2 = VectorND([1, 2, 0])
    assert v1 >= v2  # True

    # 7. Первый вектор больше по последнему элементу
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 8. Все элементы первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert not (v1 >= v2)  # False

    # 9. Первый вектор имеет одинаковые компоненты, кроме одного большего
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 10. Первый вектор равен нулевому вектору
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([0, 0, 0])
    assert v1 >= v2  # True


# Тесты на длину вектора (abs)
def test_abs():
    assert abs(VectorND([3, 4])) == 5
    assert isclose(abs(VectorND([1, 2, 2])), 3)


# Тесты на преобразование в bool
def test_bool_conversion():
    assert bool(VectorND([1, 0, 0])) is True
    assert bool(VectorND([0, 0, 0])) is False


# Тесты на умножение на число
def test_multiplication():
    vector = VectorND([1, 2, 3])
    result = vector * 2
    assert result == VectorND([2, 4, 6])
    result = 2 * vector
    assert result == VectorND([2, 4, 6])


# Тесты на деление на число
def test_division():
    vector = VectorND([2, 4, 6])
    result = vector / 2
    assert result == VectorND([1, 2, 3])
    with pytest.raises(TypeError):
        _ = 2 / vector  # Операция не определена


# Тесты на сложение
def test_addition():
    vector = VectorND([1, 2, 3])
    result = vector + 1
    assert result == VectorND([2, 3, 4])
    result = 1 + vector
    assert result == VectorND([2, 3, 4])
    result = vector + VectorND([1, 1, 1])
    assert result == VectorND([2, 3, 4])
    result = vector + VectorND([1])
    assert result == VectorND([2, 2, 3])


# Тесты на вычитание
def test_subtraction():
    vector = VectorND([3, 2, 1])
    result = vector - 1
    assert result == VectorND([2, 1, 0])
    result = 1 - vector
    assert result == VectorND([-2, -1, 0])
    result = vector - VectorND([1, 1, 1])
    assert result == VectorND([2, 1, 0])


# Тесты на унарный минус
def test_unary_minus():
    vector = VectorND([1, -2, 3])
    assert -vector == VectorND([-1, 2, -3])


# Тесты на преобразование в `int` и `float`
def test_conversion():
    vector = VectorND([3, 4])
    assert int(vector) == 5
    assert float(vector) == 5.0


# Тесты на скалярное произведение (@)
def test_dot_product():
    vector1 = VectorND([1, 2, 3])
    vector2 = VectorND([4, 5, 6])
    assert vector1 @ vector2 == 32
    vector3 = VectorND([1, 2])
    assert vector1 @ vector3 == 5  # Дополнение недостающих компонент нулями
