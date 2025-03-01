import numpy as np

# def get_extremum_indices(
#     ordinates: np.ndarray,
# ) -> tuple[np.ndarray, np.ndarray]:
#     if len(ordinates) < 3:
#         raise ValueError
#     ordinates = ordinates[1:-1] # Не учитываем краевые точки
#     ordinates_col = ordinates.reshape(len(ordinates), 1) # Представляем массив в виде столбца
#     mask_maximum = ((ordinates > ordinates_col) @ ordinates) == 0 # Получаем маску для максимумов
#     mask_minimum = ((ordinates < ordinates_col) @ ordinates) == 0 # Получаем маску для минимумов
#     return ordinates[mask_minimum], ordinates[mask_maximum]


# print(get_extremum_indices(np.array([1000, 1, -9, 7, 10, 7, 9, -5, 2, 10, 9, 4, 8, 1, 10, 10, 1000])))

def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ordinates) < 3:
        raise ValueError("Array length must be more or equal 3")
    mask_min = (ordinates[1:-1] < ordinates[:-2]) & (ordinates[1:-1] < ordinates[2:])
    mask_max = (ordinates[1:-1] > ordinates[:-2]) & (ordinates[1:-1] > ordinates[2:])
    indexes = np.arange(1, len(ordinates)-1)
    return indexes[mask_min], indexes[mask_max]

# ordinates = np.sin(2 * np.linspace(0, 4 * np.pi, 1000))
# indices_min_expected = np.array([187, 437, 687, 937], dtype=np.int32)
# indices_max_expected = np.array([ 62, 312, 562, 812], dtype=np.int32)
# 
# indices_min, indices_max = get_extremum_indices(ordinates)
# 
# assert np.allclose(indices_min, indices_min_expected)
# assert np.allclose(indices_max, indices_max_expected)