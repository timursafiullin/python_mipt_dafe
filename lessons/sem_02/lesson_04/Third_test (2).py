# import numpy as np
# import pytest
# from Code.third_task import get_dominant_color_info  # Замените на реальное имя вашего модуля
#
# # Тест 1: Простой случай с однотонным изображением
# def test_single_color_image():
#     image = np.array([[100, 100], [100, 100]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 100.0), f"Expected (100, 100.0), but got {result}"
#
# # Тест 2: Изображение с несколькими различимыми цветами
# def test_multiple_colors_image():
#     image = np.array([[100, 150], [150, 200]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (150, 50.0), f"Expected (150, 50.0), but got {result}"
#
# # Тест 3: Изображение с неразличимыми цветами, порог 10
# def test_undistinguishable_colors():
#     image = np.array([[100, 105], [103, 107]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 100.0), f"Expected (100, 100.0), but got {result}"
#
# # Тест 4: Исключение при значении threshold < 1
# def test_invalid_threshold():
#     image = np.array([[100, 100], [100, 100]], dtype=np.uint8)
#     threshold = 0
#     with pytest.raises(ValueError):
#         get_dominant_color_info(image, threshold)
#         assert False
#     assert True
#
#
# # Тест 6: Случай с несколькими группами похожих цветов
# def test_several_similar_colors():
#     image = np.array([[100, 105], [105, 110]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (105, 100.0), f"Expected (105, 100.0), but got {result}"
#
# # Тест 7: Изображение, где каждый пиксель уникален
# def test_unique_colors():
#     image = np.array([[1, 2], [3, 4]], dtype=np.uint8)
#     threshold = 1
#     result = get_dominant_color_info(image, threshold)
#     assert result == (1, 25.0), f"Expected (1, 25.0), but got {result}"
#
#
# # Тест 8: Изображение с одинаковыми пикселями, но различные по яркости (порог 10)
# def test_different_brightness_with_threshold():
#     image = np.array([[100, 110], [105, 115]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (105, 100.0), f"Expected (105, 100.0), but got {result}"
#
# # Тест 9: Изображение с одним пикселем
# def test_single_pixel_image():
#     image = np.array([[50]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (50, 100.0), f"Expected (50, 100.0), but got {result}"
#
# # Тест 10: Изображение с одинаковыми цветами, но меньше 100% совпадения (порог 5)
# def test_multiple_similar_colors_not_all_identical():
#     image = np.array([[100, 103], [105, 100]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 75.0), f"Expected (100, 75.0), but got {result}"
#
# # Тест 11: Порог равен 1
# def test_threshold_one():
#     image = np.array([[50, 51], [49, 50]], dtype=np.uint8)
#     threshold = 1
#     result = get_dominant_color_info(image, threshold)
#     assert result == (50, 100.0), f"Expected (50, 100.0), but got {result}"
#
#
# # Тест 13: Изображение с равными группами цветов, порог 10
# def test_equal_groups_of_colors():
#     image = np.array([[50, 60], [50, 60]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (50, 50.0), f"Expected (50, 50.0), but got {result}"
#
# # Тест 14: Изображение с двумя пикселями разных цветов, порог 10
# def test_two_pixels_diff_colors_with_threshold():
#     image = np.array([[100, 200]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 50.0), f"Expected (100, 50.0), but got {result}"
#
# # Тест 15: Изображение с большими однотонными областями, порог 5
# def test_large_homogeneous_area():
#     image = np.array([[50, 50, 50], [50, 50, 50], [50, 50, 50]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (50, 100.0), f"Expected (50, 100.0), but got {result}"
#
# # Тест 16: Сложное изображение с несколькими различимыми цветами и порог 15
# def test_complex_image_with_multiple_colors():
#     image = np.array([[10, 25, 50], [100, 150, 200]], dtype=np.uint8)
#     threshold = 15
#     result = get_dominant_color_info(image, threshold)
#     assert result == (50, 25.0), f"Expected (50, 25.0), but got {result}"
#
# # Тест 17: Изображение с одним сильно преобладающим цветом
# def test_dominant_color_with_small_variation():
#     image = np.array([[100, 100], [100, 100], [100, 150]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 83.33), f"Expected (100, 83.33), but got {result}"
#
# # Тест 18: Изображение с маленькими различиями и большим порогом
# def test_large_threshold_with_small_differences():
#     image = np.array([[100, 101], [102, 103]], dtype=np.uint8)
#     threshold = 10
#     result = get_dominant_color_info(image, threshold)
#     assert result == (100, 100.0), f"Expected (100, 100.0), but got {result}"
#
# # Тест 19: Изображение с большим количеством цветов, порог 5
# def test_multiple_colors_with_threshold():
#     image = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]], dtype=np.uint8)
#     threshold = 5
#     result = get_dominant_color_info(image, threshold)
#     assert result == (5, 16.6667), f"Expected (5, 16.6667), but got {result}"
#
# # Тест 20: Изображение с яркими цветами и большим порогом
# def test_bright_colors_with_large_threshold():
#     image = np.array([[255, 240], [255, 250]], dtype=np.uint8)
#     threshold = 20
#     result = get_dominant_color_info(image, threshold)
#     assert result == (255, 100.0), f"Expected (255, 100.0), but got {result}"




import numpy as np
import pytest
from solutions import get_dominant_color_info  # Замените на реальный импорт

# Тест 1: Однотонное изображение
def test_uniform_image():
    image = np.full((10, 10), 150, dtype=np.uint8)
    result = get_dominant_color_info(image, 5)
    assert result == (150, 100.0)

# Тест 2: Смежные цвета в пределах порога
def test_clustered_colors():
    image = np.array([
        [100, 102],
        [104, 103]
    ], dtype=np.uint8)
    result = get_dominant_color_info(image, 5)
    assert result == (100, 100.0)

# Тест 3: Несколько раздельных кластеров (исправленный)
def test_multiple_clusters():
    image = np.array([
        [50, 50, 100],
        [100, 150, 200]
    ], dtype=np.uint8)
    result = get_dominant_color_info(image, 49)
    # Ожидаемый результат: кластеры [50(2), 100(2), 150(1), 200(1)]
    # Самый большой кластер: 50 или 100 (по 2 пикселя), выбираем 50
    # Процент: 2/6 = 33.333...
    assert result == (50, pytest.approx(33.333, abs=0.001))
# Тест 4: Граничный порог (threshold = 1)
def test_edge_threshold():
    image = np.array([[100], [101]], dtype=np.uint8)
    result = get_dominant_color_info(image, 1)
    assert result == (100, 100.0)

# Тест 5: Минимальное значение цвета
def test_min_color():
    image = np.zeros((5, 5), dtype=np.uint8)
    result = get_dominant_color_info(image, 5)
    assert result == (0, 100.0)

# Тест 6: Максимальное значение цвета
def test_max_color():
    image = np.full((3, 3), 255, dtype=np.uint8)
    result = get_dominant_color_info(image, 10)
    assert result == (255, 100.0)

# Тест 7: Ничья между кластерами (исправленный)
def test_tie_clusters():
    image = np.array([
        [50, 50, 100, 100],
        [150, 150, 200, 200]
    ], dtype=np.uint8)
    result = get_dominant_color_info(image, 10)
    # Ожидаемый результат: 4 кластера по 2 пикселя (50,100,150,200)
    # Выбираем минимальный цвет 50 с 2/8 = 25%
    assert result == (50, 25.0)

# Тест 8: Все цвета объединяются
def test_mega_cluster():
    image = np.array([10, 15, 20, 25], dtype=np.uint8).reshape(2, 2)
    result = get_dominant_color_info(image, 10)
    assert result[1] == 100.0

# Тест 9: Один пиксель
def test_single_pixel():
    image = np.array([[128]], dtype=np.uint8)
    result = get_dominant_color_info(image, 5)
    assert result == (128, 100.0)

# Тест 10: Некорректный порог
def test_invalid_threshold():
    image = np.array([[0]], dtype=np.uint8)
    with pytest.raises(ValueError):
        get_dominant_color_info(image, 0)

# Тест 11: Большое изображение
def test_large_image():
    image = np.random.randint(100, 105, (1000, 1000), dtype=np.uint8)
    result = get_dominant_color_info(image, 5)
    assert result[1] == 100.0

# Тест 12: Ничья внутри кластера
def test_inner_tie():
    image = np.array([
        [100, 100, 102, 102],
        [100, 102, 102, 100]
    ], dtype=np.uint8)
    result = get_dominant_color_info(image, 3)
    assert result[0] == 100

# Тест 13: Цепочка объединений
def test_chain_union():
    image = np.array([50, 55, 60, 65], dtype=np.uint8).reshape(2, 2)
    result = get_dominant_color_info(image, 5)
    assert result[0] == 50 and result[1] == 100.0

# Тест 14: Все цвета разные с порогом 0 (invalid)
def test_all_unique_invalid():
    image = np.array([0, 1, 2, 3], dtype=np.uint8).reshape(2, 2)
    with pytest.raises(ValueError):
        get_dominant_color_info(image, 0)

# Тест 15: Реальные данные с плавающей разницей
def test_real_case():
    image = np.array([
        [80, 82, 85],
        [88, 90, 95],
        [100, 105, 110]
    ], dtype=np.uint8)
    result = get_dominant_color_info(image, 10)
    assert result == (80, 100.0)