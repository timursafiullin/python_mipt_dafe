import numpy as np
import pytest
from solutions import (
    get_most_profitable_month_name,
    get_mean_profit,
    sort_month_names_by_profits,
    Strategies,
    InconsistentDataError
)

"""
Тесты для задачи 1: Самый прибыльный месяц
"""
@pytest.mark.parametrize("amounts, prices, expected", [
    (np.array([[10, 20], [30, 40], [50, 60], [70, 80], [90, 100], [110, 120],
                [130, 140], [150, 160], [170, 180], [190, 200], [210, 220], [230, 240]]),
     np.array([5, 10]),
     "December"),
    (np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
                [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24]]),
     np.array([2, 3]),
     "December"),
])
def test_get_most_profitable_month(amounts, prices, expected):
    assert get_most_profitable_month_name(amounts, prices) == expected

@pytest.mark.parametrize("amounts, prices", [
    (np.array([[10, 20], [30, 40]]), np.array([5, 10, 15])),
    (np.array([[1, 2], [3, 4], [5, 6]]), np.array([2]))
])
def test_get_most_profitable_month_inconsistent_data(amounts, prices):
    with pytest.raises(InconsistentDataError):
        get_most_profitable_month_name(amounts, prices)

"""
Тесты для задачи 2: Подсчет среднего дохода
"""
@pytest.mark.parametrize("amounts, prices, strategy, expected", [
    (np.array([[10, 20], [30, 40], [50, 60], [70, 80], [90, 100], [110, 120],
                [130, 140], [150, 160], [170, 180], [190, 200], [210, 220], [230, 240]]),
     np.array([5, 10]),
     None,
     1900.0),
    (np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
                [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24]]),
     np.array([2, 3]),
     Strategies.BY_MONTH,
     np.array([8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118])/2)
])
def test_calculate_average_revenue(amounts, prices, strategy, expected):
    result = get_mean_profit(amounts, prices, strategy)
    if isinstance(result, np.ndarray):
        assert np.allclose(result, expected)
    else:
        assert result == expected

"""
Тесты для задачи 3: Сортировка месяцев по доходу
"""
@pytest.mark.parametrize("amounts, prices, ascending, expected", [
    (np.array([[10, 20], [30, 40], [50, 60], [70, 80], [90, 100], [110, 120],
                [130, 140], [150, 160], [170, 180], [190, 200], [210, 220], [230, 240]]),
     np.array([5, 10]),
     True,
     ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]),
    (np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
                [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24]]),
     np.array([2, 3]),
     False,
     ["December", "November", "October", "September", "August", "July", "June", "May", "April", "March", "February", "January"]),
])
def test_sort_month_names_by_profits(amounts, prices, ascending, expected):
    assert sort_month_names_by_profits(amounts, prices, ascending) == expected

@pytest.mark.parametrize("amounts, prices, expected", [
    (np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),
     np.array([5, 10]),
     "January"),
    (np.array([[100, 200], [300, 400], [500, 600], [700, 800], [900, 1000], [1100, 1200],
                [1300, 1400], [1500, 1600], [1700, 1800], [1900, 2000], [2100, 2200], [2300, 2400]]),
     np.array([1, 1]),
     "December"),
])
def test_get_most_profitable_month_edge_cases(amounts, prices, expected):
    assert get_most_profitable_month_name(amounts, prices) == expected
