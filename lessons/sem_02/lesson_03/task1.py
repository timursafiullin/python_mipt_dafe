import numpy as np

class ShapeMismatchError(Exception):
    pass

def sum_arrays_naive(
    lhs: list[float],
    rhs: list[float],
) -> list[float]:
    if len(lhs) != len(rhs):
        raise ShapeMismatchError
    
    return [
        elem_lhs + elem_rhs for elem_lhs, elem_rhs in zip(lhs, rhs)
    ]

def compute_poly_naive(abscissa: list[float]) -> list[float]:
    return [3 * (x ** 2) + 2 * x + 1 for x in abscissa]

def get_mutual_l2_distances_naive(
    lhs: list[list[float]],
    rhs: list[list[float]],
) -> list[list[float]]:    
    if len(lhs[0]) != len(rhs[0]):
        raise ShapeMismatchError
    
    return [
        [
            sum(
                (lhs[i][k] - rhs[j][k]) ** 2 for k in range(len(lhs[0]))
            ) ** 0.5
            for j in range(len(rhs))
        ]
        for i in range(len(lhs))
    ]

def sum_arrays_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if lhs.shape != rhs.shape:
        raise ShapeMismatchError
    return lhs + rhs

def compute_poly_vectorized(abscissa: np.ndarray) -> np.ndarray:
    return 3*(abscissa**2) + 2*abscissa + 1

def get_mutual_l2_distances_vectorized(
    lhs: np.ndarray,
    rhs: np.ndarray,
) -> np.ndarray:
    if len(lhs[0]) != len(rhs[0]):
        raise ShapeMismatchError
    return np.sqrt(np.sum((lhs[:, np.newaxis] - rhs)**2, axis=2))

def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape != azimuth.shape != inclination.shape:
        raise ShapeMismatchError
    abscissa = distances * np.sin(inclination) * np.cos(azimuth)
    ordinates = distances * np.sin(inclination) * np.sin(azimuth)
    applicates = distances * np.cos(inclination)
    return abscissa, ordinates, applicates


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape != applicates.shape:
        raise ShapeMismatchError
    azimuth = np.arctan2(ordinates, abscissa)
    distances = (abscissa**2 + ordinates**2 + applicates**2)**0.5
    inclination = np.arccos(applicates / distances)

    return distances, azimuth, inclination