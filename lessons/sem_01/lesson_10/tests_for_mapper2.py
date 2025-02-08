import pytest

# from Generators.second_dot_second_mapper_TOP import mapper
from mapper import mapper


def test_mapper_policy_long():
    result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=0))
    assert result == [4, 2]

def test_mapper_policy_short():
    result = list(mapper(lambda x, y: x + y, [1, 2], [3, 4], policy="short"))
    assert result == [4, 6]

def test_mapper_policy_invalid():
    with pytest.raises(ValueError):
        list(mapper(lambda x, y: x + y, [1, 2], [3], policy="invalid"))

def test_mapper_fillvalue_iterable():
    result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=[0, 1]))
    assert result == [4, 3]

def test_mapper_fillvalue_non_iterable():
    result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=0))
    assert result == [4, 2]

def test_mapper_long_policy_with_fillvalue_single_value():
    result = list(
        mapper(
            lambda x, y: x + y,
            [1, 2],
            [3],
            policy="long",
            fillvalue=0
        )
    )
    assert result == [4, 2]

def test_mapper_long_policy_with_fillvalue_iterable():
    result = list(
        mapper(
            lambda x, y: x + y,
            [1, 2],
            [3],
            policy="long",
            fillvalue=[5]
        )
    )
    assert result == [4, 7]

def test_mapper_long_policy_fillvalue_mismatched_size():
    result = list(
        mapper(
            lambda x, y: x + y,
            [1, 2],
            [3],
            policy="long",
            fillvalue=[10, 20]
        )
    )
    assert result == [4, 22]

def test_mapper_invalid_policy():
    with pytest.raises(ValueError):
        list(mapper(lambda x: x, [1, 2], policy="invalid_policy"))

def test_mapper_short_policy_default():
    result = list(
        mapper(
            lambda x, y: x * y,
            [1, 2, 3],
            [4, 5],
            policy="short"
        )
    )
    assert result == [4, 10]

def test_mapper_long_policy_no_fillvalue():
    with pytest.raises(ValueError):
        result = list(
            mapper(
                lambda x, y: x * y,
                [1, 2],
                [3],
                policy="long"
            )
        )

def test_mapper_long_policy_with_iterable_fillvalue_different_sizes():
    result = list(
        mapper(
            lambda x, y, z: x + y + z,
            [1],
            [2, 3],
            [4, 5, 6],
            policy="long",
            fillvalue=[10, 20, 30]
        )
    )
    assert result == [7, 18, 36]

def test_mapper_short_policy_with_large_inputs():
    result = list(
        mapper(
            lambda x, y: x + y,
            range(1000),
            range(500),
            policy="short"
        )
    )
    assert result == [x * 2 for x in range(500)]

def test_mapper_long_policy_fillvalue_large_inputs():
    result = list(
        mapper(
            lambda x, y: x - y,
            range(1000),
            range(500),
            policy="long",
            fillvalue=10
        )
    )
    assert result[500:510] == [490, 491, 492, 493, 494, 495, 496, 497, 498, 499]

def test_mapper_empty_iterables_long_policy():
    result = list(
        mapper(
            lambda x, y: x + y,
            [],
            [],
            policy="long",
            fillvalue=0
        )
    )
    assert result == []

def test_mapper_long_policy_with_non_iterable_fillvalue():
    result = list(
        mapper(
            lambda x, y: x + y,
            [1, 2, 3],
            [4, 5],
            policy="long",
            fillvalue=10
        )
    )
    assert result == [5, 7, 13]

def test_mapper_fillvalue_non_iterable_mismatch():
    result = list(
        mapper(
            lambda x, y: x + y,
            [1, 2],
            [3],
            policy="long",
            fillvalue=100
        )
    )
    assert result == [4, 102]

def test_mapper_multiple_iterables_with_short_policy():
    result = list(
        mapper(
            lambda x, y, z: x + y + z,
            [1, 2, 3],
            [4, 5],
            [6, 7, 8],
            policy="short"
        )
    )
    assert result == [11, 14]

def test_mapper_multiple_iterables_with_long_policy():
    result = list(
        mapper(
            lambda x, y, z: x + y + z,
            [1, 2, 3],
            [4, 5],
            [6],
            policy="long",
            fillvalue=0
        )
    )
    assert result == [11, 7, 3]

def test_mapper_fillvalue_as_empty_iterable():
    with pytest.raises(ValueError):
        result = list(
            mapper(
                lambda x, y: x + y,
                [1, 2],
                [3],
                policy="long",
                fillvalue=[]
            )
        )
