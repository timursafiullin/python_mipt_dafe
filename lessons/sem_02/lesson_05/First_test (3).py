import pytest
import numpy as np


class ShapeMismatchError(Exception):
    pass

from tasks import can_satisfy_demand


@pytest.mark.parametrize("costs, resource_amounts, demand_expected, expected", [
    # 1. Базовый случай: хватает ресурсов
    (np.array([[2, 3], [1, 2]]), np.array([10, 6]), np.array([2, 2]), True),
    # 2. Недостаточно ресурсов
    (np.array([[2, 3], [1, 2]]), np.array([4, 3]), np.array([2, 2]), False),
    # 3. Ресурсы впритык
    (np.array([[2, 3], [1, 2]]), np.array([10, 6]), np.array([2, 2]), True),
    # 4. Нулевой спрос
    (np.array([[2, 3], [1, 2]]), np.array([10, 6]), np.array([0, 0]), True),
    # 5. Нулевые ресурсы
    (np.array([[2, 3], [1, 2]]), np.array([0, 0]), np.array([2, 2]), False),
    # 6. Один товар, один ресурс, хватает
    (np.array([[5]]), np.array([10]), np.array([2]), True),
    # 7. Один товар, один ресурс, не хватает
    (np.array([[5]]), np.array([4]), np.array([2]), False),
    # 8. Большая матрица, хватает ресурсов
    (np.ones((5, 5)), np.array([10, 10, 10, 10, 10]), np.array([1, 1, 1, 1, 1]), True),
    # 9. Большая матрица, не хватает ресурсов
    (np.ones((5, 5)), np.array([2, 2, 2, 2, 2]), np.array([1, 1, 1, 1, 1]), False),
    # 14. Производство требует больше ресурсов, чем имеется
    (np.array([[10, 20], [30, 40]]), np.array([5, 5]), np.array([1, 1]), False),
    # 15. Производство возможно только с точным расчетом
    (np.array([[1, 2], [3, 4]]), np.array([5, 11]), np.array([1, 2]), True)
])
def test_can_meet_demand(costs, resource_amounts, demand_expected, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            can_satisfy_demand(costs, resource_amounts, demand_expected)
    else:
        assert can_satisfy_demand(costs, resource_amounts, demand_expected) == expected

