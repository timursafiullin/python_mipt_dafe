import pytest
from task1 import ShapeMismatchError
from task1 import sum_arrays_vectorized, sum_arrays_naive, compute_poly_vectorized 

from task1 import get_mutual_l2_distances_vectorized, get_mutual_l2_distances_naive
import numpy as np

# Тесты для корректных случаев
def test_sum_arrays_basic():
    result = sum_arrays_vectorized(np.array([1, 2, 3]), np.array([4, 5, 6]))
    print(result)
    assert np.array_equal(result, np.array([5, 7, 9]))

def test_sum_arrays_with_negatives():
    result = sum_arrays_vectorized(np.array([-1, -2, -3]), np.array([1, 2, 3]))
    assert np.array_equal(result, np.array([0, 0, 0]))

def test_sum_arrays_with_zeros():
    result = sum_arrays_vectorized(np.array([0, 0, 0]), np.array([1, 2, 3]))
    assert np.array_equal(result, np.array([1, 2, 3]))

def test_sum_arrays_with_floats():
    result = sum_arrays_vectorized(np.array([0.1, 0.2, 0.3]), np.array([0.4, 0.5, 0.6]))
    assert np.allclose(result, np.array([0.5, 0.7, 0.9]))

def test_sum_arrays_large_numbers():
    result = sum_arrays_vectorized(np.array([1e9, 2e9, 3e9]), np.array([1e9, 2e9, 3e9]))
    assert np.array_equal(result, np.array([2e9, 4e9, 6e9]))

def test_sum_arrays_one_element():
    result = sum_arrays_vectorized(np.array([42]), np.array([8]))
    assert np.array_equal(result, np.array([50]))

def test_sum_arrays_empty():
    result = sum_arrays_vectorized(np.array([]), np.array([]))
    assert np.array_equal(result, np.array([]))

def test_sum_arrays_nan_values():
    result = sum_arrays_vectorized(np.array([np.nan, 2]), np.array([1, 2]))
    assert np.isnan(result[0]) and result[1] == 4

def test_sum_arrays_inf_values():
    result = sum_arrays_vectorized(np.array([np.inf, 1]), np.array([-np.inf, 1]))
    assert np.isnan(result[0]) and result[1] == 2

def test_sum_arrays_mixed_int_float():
    result = sum_arrays_vectorized(np.array([1, 2, 3], dtype=int), np.array([0.5, 1.5, 2.5]))
    assert np.allclose(result, np.array([1.5, 3.5, 5.5]))

# Тесты на ошибки
def test_sum_arrays_shape_mismatch():
    with pytest.raises(ShapeMismatchError):
        sum_arrays_vectorized(np.array([1, 2, 3]), np.array([1, 2]))

def test_sum_arrays_large_arrays():
    arr1 = np.ones(10**6)
    arr2 = np.ones(10**6)
    result = sum_arrays_vectorized(arr1, arr2)
    assert np.array_equal(result, np.full(10**6, 2))

def test_sum_arrays_int_overflow():
    arr1 = np.array([2**31 - 1, 2**31 - 1])
    arr2 = np.array([1, 1])
    result = sum_arrays_vectorized(arr1, arr2)
    assert np.array_equal(result, np.array([2**31, 2**31]))

def test_sum_arrays_repeated_values():
    result = sum_arrays_vectorized(np.array([1, 1, 1, 1]), np.array([2, 2, 2, 2]))
    assert np.array_equal(result, np.array([3, 3, 3, 3]))

def test_sum_arrays_negative_floats():
    result = sum_arrays_vectorized(np.array([-0.1, -0.2, -0.3]), np.array([0.1, 0.2, 0.3]))
    assert np.array_equal(result, np.array([0, 0, 0]))

def test_sum_arrays_different_dtypes():
    result = sum_arrays_vectorized(np.array([1, 2, 3], dtype=int), np.array([1.5, 2.5, 3.5], dtype=float))
    assert np.allclose(result, np.array([2.5, 4.5, 6.5]))

def test_sum_arrays_step_values():
    result = sum_arrays_vectorized(np.arange(0, 10, 2), np.arange(0, 10, 2))
    assert np.array_equal(result, np.array([0, 4, 8, 12, 16]))

def test_sum_arrays_large_step():
    result = sum_arrays_vectorized(np.array([0, 5, 10]), np.array([10, 15, 20]))
    assert np.array_equal(result, np.array([10, 20, 30]))

def test_sum_arrays_huge_values():
    result = sum_arrays_vectorized(np.array([1e100, 2e100]), np.array([1e100, 2e100]))
    assert np.array_equal(result, np.array([2e100, 4e100]))



from task1 import compute_poly_naive
"""
Тесты для полинома
"""
# Тесты для стандартных случаев
def test_compute_poly_standard():
    x = np.array([0, 1, 2, 3])
    result = compute_poly_vectorized(x)
    expected = compute_poly_naive(x)
    assert np.array_equal(result, expected)

def test_compute_poly_negative_values():
    x = np.array([-1, -2, -3])
    result = compute_poly_vectorized(x)
    expected = compute_poly_naive(x)
    assert np.array_equal(result, expected)

def test_compute_poly_large_values():
    x = np.array([100, 200, 300])
    result = compute_poly_vectorized(x)
    expected = compute_poly_naive(x)
    assert np.array_equal(result, expected)

def test_compute_poly_with_fractions():
    x = np.array([0.5, 1.5, 2.5])
    result = compute_poly_vectorized(x)
    expected = np.array([2.75, 10.75, 24.75])
    assert np.allclose(result, expected)

def test_compute_poly_large_negative_values():
    x = np.array([-100, -200, -300])
    result = compute_poly_vectorized(x)
    expected = np.array([29801, 119601, 269401])
    assert np.array_equal(result, expected)

def test_compute_poly_single_value():
    x = np.array([10])
    result = compute_poly_vectorized(x)
    expected = np.array([321])
    assert np.array_equal(result, expected)

def test_compute_poly_empty_array():
    x = np.array([])
    result = compute_poly_vectorized(x)
    expected = np.array([])
    assert np.array_equal(result, expected)

def test_compute_poly_zeros():
    x = np.zeros(5)
    result = compute_poly_vectorized(x)
    expected = np.array([1, 1, 1, 1, 1])
    assert np.array_equal(result, expected)

# Тесты с разными типами данных
def test_compute_poly_integer_values():
    x = np.array([1, 2, 3], dtype=int)
    result = compute_poly_vectorized(x)
    expected = np.array([6, 17, 34])
    assert np.array_equal(result, expected)

def test_compute_poly_mixed_dtypes():
    x = np.array([1, 2.5, -3], dtype=float)
    result = compute_poly_vectorized(x)
    expected = np.array([6, 24.75, 22])
    assert np.allclose(result, expected)

def test_compute_poly_large_array():
    x = np.arange(1000)
    result = compute_poly_vectorized(x)
    assert len(result) == 1000 and result[0] == 1 and result[-1] == 3*(999**2) + 2*999 + 1

def test_compute_poly_huge_numbers():
    x = np.array([1e10, -1e10])
    result = compute_poly_vectorized(x)
    expected = np.array([3e20 + 2e10 + 1, 3e20 - 2e10 + 1])
    assert np.allclose(result, expected)

def test_compute_poly_small_numbers():
    x = np.array([1e-10, -1e-10])
    result = compute_poly_vectorized(x)
    expected = np.array([1, 1])  # Очень маленькие x не влияют на результат
    assert np.allclose(result, expected)

def test_compute_poly_repeated_values():
    x = np.array([2, 2, 2, 2])
    result = compute_poly_vectorized(x)
    expected = np.array([17, 17, 17, 17])
    assert np.array_equal(result, expected)

def test_compute_poly_alternating_signs():
    x = np.array([-1, 1, -2, 2, -3, 3])
    result = compute_poly_vectorized(x)
    expected = np.array([2, 6, 9, 17, 22, 34])
    assert np.array_equal(result, expected)

def test_compute_poly_random_values():
    np.random.seed(42)
    x = np.random.uniform(-10, 10, 5)
    result = compute_poly_vectorized(x)
    expected = 3 * x**2 + 2 * x + 1
    assert np.allclose(result, expected)




"""
Третья задача
"""


def test_get_mutual_l2_distances_basic():
    lhs = [[0, 0], [1, 1]]
    rhs = [[1, 0], [0, 1]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_single_row():
    lhs = [[3, 4]]
    rhs = [[0, 0], [3, 4]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_identity():
    lhs = [[1, 2, 3], [4, 5, 6]]
    rhs = [[1, 2, 3], [4, 5, 6]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_different_sizes():
    lhs = [[0, 0], [1, 1], [2, 2]]
    rhs = [[3, 3], [4, 4]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_large_values():
    lhs = [[1000, 2000], [3000, 4000]]
    rhs = [[5000, 6000], [7000, 8000]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_negative_values():
    lhs = [[-1, -2], [-3, -4]]
    rhs = [[5, 6], [-7, -8]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_floats():
    lhs = [[1.5, 2.5], [3.5, 4.5]]
    rhs = [[0.5, 1.5], [2.5, 3.5]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)

def test_get_mutual_l2_distances_high_dimension():
    lhs = [[1, 2, 3, 4], [5, 6, 7, 8]]
    rhs = [[9, 10, 11, 12], [13, 14, 15, 16]]
    result_vectorized = get_mutual_l2_distances_vectorized(np.array(lhs), np.array(rhs))
    result_naive = get_mutual_l2_distances_naive(lhs, rhs)
    assert np.allclose(result_vectorized, result_naive)




