import pytest
from range_float import range_float

def test_range_float_default():
    result = list(range_float(stop=5))
    assert result == [0.0, 1.0, 2.0, 3.0, 4.0]

    result = list(range_float(stop=2))
    assert result == [0.0, 1.0]

def test_range_float_with_start():
    result = list(range_float(start=2, stop=5))
    assert result == [2.0, 3.0, 4.0]

def test_range_float_with_step():
    result = list(range_float(start=1, stop=5, step=0.5))
    assert result == [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    result = list(range_float(start=0.5, stop=2, step=0.5))
    assert result == [0.5, 1.0, 1.5]

def test_range_float_negative_step():
    result = list(range_float(start=5, stop=1, step=-1))
    assert result == [5.0, 4.0, 3.0, 2.0]

def test_range_float_empty():
    result = list(range_float(start=5, stop=5))
    assert result == []

def test_diff_signs():
    with pytest.raises(ValueError):
        list(range_float(start=2, stop=-5, step=1))
    
    with pytest.raises(ValueError):
        list(range_float(start=-5, stop=5, step=-1))
    
    result = list(range_float(start=1, stop=5, step=1))
    assert result

    result = list(range_float(start=5, stop=-10, step=-2))
    assert result

def test_range_float_invalid_stop():
    with pytest.raises(TypeError):
        list(range_float(start=1, step=0.5))  # stop не указан

def test_range_float_zero_step():
    with pytest.raises(ValueError):
        list(range_float(start=1, stop=5, step=0))

def test_range_float_non_numeric_inputs():
    with pytest.raises(TypeError):
        list(range_float(start="1", stop=5, step=0.5))
    with pytest.raises(TypeError):
        list(range_float(start=1, stop="5", step=0.5))
    with pytest.raises(TypeError):
        list(range_float(start=1, stop=5, step="0.5"))

def test_range_float_large_numbers():
    result = list(range_float(start=1000000, stop=1000005, step=0.1))
    corresult = [1000000.0, 1000000.1, 1000000.2, 1000000.3, 1000000.4, 1000000.5, 1000000.6, 1000000.7, 1000000.8, 1000000.9, 1000001.0, 1000001.1, 1000001.2, 1000001.3, 1000001.4, 1000001.5, 1000001.6, 1000001.7, 1000001.8, 1000001.9, 1000002.0, 1000002.1, 1000002.2, 1000002.3, 1000002.4, 1000002.5, 1000002.6, 1000002.7, 1000002.8, 1000002.9, 1000003.0, 1000003.1, 1000003.2, 1000003.3, 1000003.4, 1000003.5, 1000003.6, 1000003.7, 1000003.8, 1000003.9, 1000004.0, 1000004.1, 1000004.2, 1000004.3, 1000004.4, 1000004.5, 1000004.6, 1000004.7, 1000004.8, 1000004.9]
    for a, b in zip(result, corresult):
        assert (a-b) < 1e-6

def test_range_float_very_small_step():
    result = list(range_float(start=0, stop=1, step=0.01))
