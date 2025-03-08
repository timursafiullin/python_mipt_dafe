import numpy as np
import pytest

from tasks import get_projections_components as compute_projections, ShapeMismatchError  # Замени `your_module` на имя твоего файла

def test_valid_basis():
    """Матрица является базисом, проверяем проекции и ортогональные составляющие"""
    matrix = np.array([[1, 0], [0, 1]])
    vector = np.array([3, 4])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.array([[3, 0], [0, 4]])
    expected_orthogonal = np.array([[0, 4], [3, 0]])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_non_basis_matrix():
    """Матрица не является базисом (линейно зависимые строки)"""
    matrix = np.array([[1, 1], [2, 2]])
    vector = np.array([3, 4])
    projections, orthogonal_components = compute_projections(matrix, vector)

    assert projections is None
    assert orthogonal_components is None

def test_3d_valid_basis():
    """Проверка для 3D ортонормированного базиса"""
    matrix = np.eye(3)  # Ортонормированный базис
    vector = np.array([1, 2, 3])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.diag([1, 2, 3])
    expected_orthogonal = np.array([[0, 2, 3], [1, 0, 3], [1, 2, 0]])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_non_square_matrix():
    """Матрица не квадратная — должно быть исключение"""
    matrix = np.array([[1, 0, 0], [0, 1, 0]])
    vector = np.array([1, 2, 3])

    with pytest.raises(ShapeMismatchError):
        compute_projections(matrix, vector)

def test_vector_dimension_mismatch():
    """Размерность вектора не совпадает с размерностью матрицы"""
    matrix = np.eye(3)
    vector = np.array([1, 2])

    with pytest.raises(ShapeMismatchError):
        compute_projections(matrix, vector)

def test_random_3d_basis():
    """Случайный базис в 3D"""
    matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    vector = np.array([5, -3, 2])
    projections, orthogonal_components = compute_projections(matrix, vector)

    assert np.allclose(projections, np.diag([5, -3, 2]))
    assert np.allclose(orthogonal_components, np.array([[0, -3, 2], [5, 0, 2], [5, -3, 0]]))

def test_singular_matrix():
    """Матрица вырожденная (имеет нулевой определитель)"""
    matrix = np.array([[1, 2], [2, 4]])
    vector = np.array([2, 2])
    projections, orthogonal_components = compute_projections(matrix, vector)

    assert projections is None
    assert orthogonal_components is None

def test_negative_values():
    """Отрицательные значения в матрице и векторе"""
    matrix = np.array([[1, 0], [0, -1]])
    vector = np.array([-3, -4])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.array([[-3, 0], [0, -4]])
    expected_orthogonal = np.array([[0, -4], [-3, 0]])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_large_numbers():
    """Работа с большими числами"""
    matrix = np.eye(2) * 1e6
    vector = np.array([1e6, -1e6])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.array([[1e6, 0], [0, -1e6]])
    expected_orthogonal = np.array([[0, -1e6], [1e6, 0]])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_ill_conditioned_matrix():
    """Матрица почти вырожденная"""
    matrix = np.array([[1, 1], [1, 1.000001]])
    vector = np.array([1, 1])
    projections, orthogonal_components = compute_projections(matrix, vector)

    # Мы не знаем точные значения, но проверяем, что нет None
    assert projections is not None
    assert orthogonal_components is not None

def test_high_dimensional_basis():
    """Проверка работы в 5D"""
    matrix = np.eye(5)
    vector = np.array([1, 2, 3, 4, 5])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.diag([1, 2, 3, 4, 5])
    expected_orthogonal = np.array([
        [0, 2, 3, 4, 5],
        [1, 0, 3, 4, 5],
        [1, 2, 0, 4, 5],
        [1, 2, 3, 0, 5],
        [1, 2, 3, 4, 0]
    ])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_zero_matrix():
    """Матрица состоит из нулей"""
    matrix = np.zeros((3, 3))
    vector = np.array([1, 2, 3])
    projections, orthogonal_components = compute_projections(matrix, vector)

    assert projections is None
    assert orthogonal_components is None

def test_identity_matrix():
    """Единичная матрица в 4D"""
    matrix = np.eye(4)
    vector = np.array([1, -1, 0, 2])
    projections, orthogonal_components = compute_projections(matrix, vector)

    expected_projections = np.diag([1, -1, 0, 2])
    expected_orthogonal = np.array([
        [0, -1, 0, 2],
        [1, 0, 0, 2],
        [1, -1, 0, 2],
        [1, -1, 0, 0]
    ])

    assert np.allclose(projections, expected_projections)
    assert np.allclose(orthogonal_components, expected_orthogonal)

def test_matrix_with_fractions():
    """Проверка работы с дробными значениями"""
    matrix = np.array([[0.5, 0.5], [-0.5, 0.5]])
    vector = np.array([1, 1])
    projections, orthogonal_components = compute_projections(matrix, vector)

    assert projections is not None
    assert orthogonal_components is not None
