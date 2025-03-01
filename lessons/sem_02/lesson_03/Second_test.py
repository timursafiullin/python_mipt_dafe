import pytest
import numpy as np
from task1 import ShapeMismatchError
from task1 import convert_to_sphere, convert_from_sphere

# ==== Тесты для convert_to_sphere ====

def test_convert_to_sphere_basic():
    x = np.array([1])
    y = np.array([0])
    z = np.array([0])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [1])
    assert np.allclose(phi, [0])
    assert np.allclose(theta, [np.pi / 2])

def test_convert_to_sphere_negative_x():
    x = np.array([-1])
    y = np.array([0])
    z = np.array([0])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [1])
    assert np.allclose(phi, [np.pi])
    assert np.allclose(theta, [np.pi / 2])

def test_convert_to_sphere_positive_z():
    x = np.array([0])
    y = np.array([0])
    z = np.array([1])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [1])
    assert np.allclose(phi, [0])
    assert np.allclose(theta, [0])

def test_convert_to_sphere_negative_z():
    x = np.array([0])
    y = np.array([0])
    z = np.array([-1])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [1])
    assert np.allclose(phi, [0])
    assert np.allclose(theta, [np.pi])

def test_convert_to_sphere_diagonal():
    x = np.array([1])
    y = np.array([1])
    z = np.array([1])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [np.sqrt(3)])
    assert np.allclose(phi, [np.pi / 4])
    assert np.allclose(theta, [np.arccos(1 / np.sqrt(3))])

def test_convert_to_sphere_multiple_points():
    x = np.array([1, 2])
    y = np.array([1, 0])
    z = np.array([1, 3])
    r, phi, theta = convert_to_sphere(x, y, z)
    expected_r = np.sqrt(x**2 + y**2 + z**2)
    expected_phi = np.arctan2(y, x)
    expected_theta = np.arccos(z / expected_r)
    assert np.allclose(r, expected_r)
    assert np.allclose(phi, expected_phi)
    assert np.allclose(theta, expected_theta)

def test_convert_to_sphere_zero_vector():
    x = np.array([0])
    y = np.array([0])
    z = np.array([0])
    # with pytest.raises(RuntimeWarning):  # Деление на ноль в arccos
    convert_to_sphere(x, y, z)

def test_convert_to_sphere_large_values():
    x = np.array([1e6])
    y = np.array([1e6])
    z = np.array([1e6])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [np.sqrt(3) * 1e6])
    assert np.allclose(phi, [np.pi / 4])
    assert np.allclose(theta, [np.arccos(1 / np.sqrt(3))])

def test_convert_to_sphere_negative_values():
    x = np.array([-1])
    y = np.array([-1])
    z = np.array([-1])
    r, phi, theta = convert_to_sphere(x, y, z)
    assert np.allclose(r, [np.sqrt(3)])
    assert np.allclose(phi, [-3 * np.pi / 4])
    assert np.allclose(theta, [np.arccos(-1 / np.sqrt(3))])

def test_convert_to_sphere_shape_mismatch():
    x = np.array([1, 2])
    y = np.array([1])
    z = np.array([1, 2])
    with pytest.raises(ShapeMismatchError):
        convert_to_sphere(x, y, z)


# ==== Тесты для convert_from_sphere ====

def test_convert_from_sphere_basic():
    r = np.array([1])
    phi = np.array([0])
    theta = np.array([np.pi / 2])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [1])
    assert np.allclose(y, [0])
    assert np.allclose(z, [0])

def test_convert_from_sphere_negative_phi():
    r = np.array([1])
    phi = np.array([-np.pi / 4])
    theta = np.array([np.pi / 2])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [np.cos(-np.pi / 4)])
    assert np.allclose(y, [np.sin(-np.pi / 4)])
    assert np.allclose(z, [0])

def test_convert_from_sphere_zero_r():
    r = np.array([0])
    phi = np.array([0])
    theta = np.array([0])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [0])
    assert np.allclose(y, [0])
    assert np.allclose(z, [0])

def test_convert_from_sphere_large_values():
    r = np.array([1e6])
    phi = np.array([np.pi / 4])
    theta = np.array([np.pi / 3])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [1e6 * np.sin(np.pi / 3) * np.cos(np.pi / 4)])
    assert np.allclose(y, [1e6 * np.sin(np.pi / 3) * np.sin(np.pi / 4)])
    assert np.allclose(z, [1e6 * np.cos(np.pi / 3)])

def test_convert_from_sphere_negative_theta():
    r = np.array([1])
    phi = np.array([np.pi / 4])
    theta = np.array([-np.pi / 3])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [np.sin(-np.pi / 3) * np.cos(np.pi / 4)])
    assert np.allclose(y, [np.sin(-np.pi / 3) * np.sin(np.pi / 4)])
    assert np.allclose(z, [np.cos(-np.pi / 3)])

def test_convert_from_sphere_multiple_points():
    r = np.array([1, 2])
    phi = np.array([0, np.pi / 2])
    theta = np.array([np.pi / 2, np.pi / 4])
    x, y, z = convert_from_sphere(r, phi, theta)
    expected_x = r * np.sin(theta) * np.cos(phi)
    expected_y = r * np.sin(theta) * np.sin(phi)
    expected_z = r * np.cos(theta)
    assert np.allclose(x, expected_x)
    assert np.allclose(y, expected_y)
    assert np.allclose(z, expected_z)

def test_convert_from_sphere_negative_values():
    r = np.array([1])
    phi = np.array([-np.pi / 4])
    theta = np.array([-np.pi / 4])
    x, y, z = convert_from_sphere(r, phi, theta)
    assert np.allclose(x, [np.sin(-np.pi / 4) * np.cos(-np.pi / 4)])
    assert np.allclose(y, [np.sin(-np.pi / 4) * np.sin(-np.pi / 4)])
    assert np.allclose(z, [np.cos(-np.pi / 4)])

def test_convert_from_sphere_shape_mismatch():
    r = np.array([1, 2])
    phi = np.array([1])
    theta = np.array([1, 2])
    with pytest.raises(ShapeMismatchError):
        convert_from_sphere(r, phi, theta)
