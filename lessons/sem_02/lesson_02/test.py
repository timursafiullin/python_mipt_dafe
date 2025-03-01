import numpy as np

class ShapeMismatchError(Exception):
    pass

def convert_from_polar(
    distances: np.ndarray,
    angles: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    
    if distances.size != angles.size:
        raise ShapeMismatchError()

    abscissa = distances * np.cos(angles)
    ordinates = distances * np.sin(angles)

    return abscissa, ordinates


def convert_to_polar(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    
    if abscissa.size != ordinates.size:
        raise ShapeMismatchError()

    distances = np.sqrt(abscissa**2 + ordinates**2)
    angles = np.arctan2(ordinates, abscissa)

    return distances, angles

abscissa = np.array([1, 0, -1, 0], dtype=np.float64)
ordinates = np.array([0, 1, 0, -1], dtype=abscissa.dtype)

distances, angles = convert_to_polar(abscissa, ordinates)
abscissa_conv, ordinates_conv = convert_from_polar(distances, angles)

print(abscissa, ordinates)
print(distances, angles)