import numpy as np
import pytest
from test import get_extremum_indices  # замените your_module на имя вашего файла

# 1. Обычный случай с несколькими экстремумами
def test_multiple_extrema():
    ordinates = np.array([1, 3, 2, 4, 1, 5, 0])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([2, 4]))
    assert np.array_equal(maxima, np.array([1, 3, 5]))

# 2. Монотонно возрастающая последовательность (нет экстремумов)
def test_monotonic_increasing():
    ordinates = np.array([1, 2, 3, 4, 5])
    minima, maxima = get_extremum_indices(ordinates)
    assert minima.size == 0
    assert maxima.size == 0

# 3. Монотонно убывающая последовательность (нет экстремумов)
def test_monotonic_decreasing():
    ordinates = np.array([5, 4, 3, 2, 1])
    minima, maxima = get_extremum_indices(ordinates)
    assert minima.size == 0
    assert maxima.size == 0

# 4. Чередование экстремумов
def test_alternating_extrema():
    ordinates = np.array([2, 5, 2, 5, 2, 5, 2])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([2, 4]))
    assert np.array_equal(maxima, np.array([1, 3, 5]))

# 5. Плоский участок без экстремумов
def test_flat_segment():
    ordinates = np.array([3, 3, 3, 3, 3])
    minima, maxima = get_extremum_indices(ordinates)
    assert minima.size == 0
    assert maxima.size == 0

# 6. Малый массив без экстремумов
def test_too_short_array():
    ordinates = np.array([2, 3])
    with pytest.raises(ValueError):
        minima, maxima = get_extremum_indices(ordinates)
        assert False
    assert True

# 7. Случай с одним экстремумом (максимум)
def test_single_maximum():
    ordinates = np.array([1, 4, 1])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([]))
    assert np.array_equal(maxima, np.array([1]))

# 8. Случай с одним экстремумом (минимум)
def test_single_minimum():
    ordinates = np.array([4, 1, 4])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([1]))
    assert np.array_equal(maxima, np.array([]))

# 9. Равные значения в начале и конце массива
def test_same_start_end():
    ordinates = np.array([3, 1, 4, 1, 3])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([1, 3]))
    assert np.array_equal(maxima, np.array([2]))

# 10. Случай с шумом (много маленьких колебаний)
def test_noisy_signal():
    ordinates = np.array([1, 3, 2, 4, 3, 5, 4])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([2, 4]))
    assert np.array_equal(maxima, np.array([1, 3, 5]))

# 11. Все точки одинаковые
def test_all_identical():
    ordinates = np.array([7, 7, 7, 7, 7])
    minima, maxima = get_extremum_indices(ordinates)
    assert minima.size == 0
    assert maxima.size == 0

# 12. Два последовательных минимума
def test_double_minimum():
    ordinates = np.array([5, 1, 2, 1, 5])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([1, 3]))
    assert np.array_equal(maxima, np.array([2]))

# 13. Два последовательных максимума
def test_double_maximum():
    ordinates = np.array([1, 5, 4, 5, 1])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([2]))
    assert np.array_equal(maxima, np.array([1, 3]))

# 14. Случай с плавным изменением без экстремумов
def test_smooth_transition():
    ordinates = np.array([1, 2, 3, 4, 5, 6, 7])
    minima, maxima = get_extremum_indices(ordinates)
    assert minima.size == 0
    assert maxima.size == 0

# 15. Случай с разрывами
def test_large_jumps():
    ordinates = np.array([1, 100, 1, 100, 1])
    minima, maxima = get_extremum_indices(ordinates)
    assert np.array_equal(minima, np.array([2]))
    assert np.array_equal(maxima, np.array([1, 3]))

def test_from_task():
    ordinates = np.sin(2 * np.linspace(0, 4 * np.pi, 1000))
    indices_min_expected = np.array([187, 437, 687, 937], dtype=np.int32)
    indices_max_expected = np.array([62, 312, 562, 812], dtype=np.int32)

    indices_min, indices_max = get_extremum_indices(ordinates)

    assert np.allclose(indices_min, indices_min_expected)
    assert np.allclose(indices_max, indices_max_expected)
