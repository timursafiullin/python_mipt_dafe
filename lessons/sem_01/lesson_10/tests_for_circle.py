import pytest

from circle import circle

def test_circle_simple():
    circle_gen = circle("abc")
    result = [next(circle_gen) for _ in range(6)]
    assert result == ["a", "b", "c", "a", "b", "c"]

def test_circle_single_element():
    circle_gen = circle("a")
    result = [next(circle_gen) for _ in range(5)]
    assert result == ["a", "a", "a", "a", "a"]

def test_circle_empty():
    with pytest.raises(ValueError):
        next(circle(""))

def test_circle_large_input():
    data = range(100)
    circle_gen = circle(data)
    result = [next(circle_gen) for _ in range(105)]
    assert result == list(data) + list(data[:5])

def test_circle_reset():
    data = "ab"
    circle_gen = circle(data)
    result = [next(circle_gen) for _ in range(10)]
    assert result == ["a", "b"] * 5

def test_circle_non_iterable():
    circle(None)

import pytest

def test_circle_with_string():
    gen = circle("abc")
    assert next(gen) == "a"
    assert next(gen) == "b"
    assert next(gen) == "c"
    assert next(gen) == "a"
    assert next(gen) == "b"

def test_circle_with_list():
    gen = circle([1, 2, 3])
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 1
    assert next(gen) == 2

def test_circle_with_tuple():
    gen = circle((10, 20, 30))
    assert next(gen) == 10
    assert next(gen) == 20
    assert next(gen) == 30
    assert next(gen) == 10

def test_circle_with_single_element():
    gen = circle([42])
    assert next(gen) == 42
    assert next(gen) == 42
    assert next(gen) == 42

def test_circle_with_empty_iterable():
    with pytest.raises(ValueError):
        gen = circle([])
        next(gen)

def test_circle_with_generator_input():
    gen_input = (x**2 for x in range(3))
    gen = circle(gen_input)
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 4

def test_circle_with_large_iterable():
    gen = circle(range(1, 1001))
    for i in range(1, 1001):
        assert next(gen) == i
    assert next(gen) == 1  # Cycle restarts

def test_circle_with_non_iterable_input():
    with pytest.raises(TypeError):
        gen = circle(42)
        next(gen)

def test_circle_with_mutable_iterable():
    lst = [1, 2, 3]
    gen = circle(lst)
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3

def test_circle_with_multiple_cycles():
    gen = circle("xy")
    assert [next(gen) for _ in range(10)] == ["x", "y", "x", "y", "x", "y", "x", "y", "x", "y"]

def test_circle_with_infinite_loop_simulation():
    gen = circle([0, 1])
    for _ in range(1000):
        assert next(gen) in [0, 1]

def test_circle_with_custom_objects():
    class Custom:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"Custom({self.name})"

    objects = [Custom("A"), Custom("B")]
    gen = circle(objects)
    assert repr(next(gen)) == "Custom(A)"
    assert repr(next(gen)) == "Custom(B)"
    assert repr(next(gen)) == "Custom(A)"

def test_circle_with_iterator():
    iterable = iter([1, 2, 3])
    gen = circle(iterable)
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3

def test_circle_with_boolean_input():
    gen = circle([True, False])
    assert next(gen) is True
    assert next(gen) is False
    assert next(gen) is True

def test_circle_with_complex_numbers():
    gen = circle([1 + 2j, 3 + 4j])
    assert next(gen) == 1 + 2j
    assert next(gen) == 3 + 4j
    assert next(gen) == 1 + 2j

