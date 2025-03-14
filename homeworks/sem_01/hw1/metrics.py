from uuid import UUID
from typing import Sequence
from numbers import Real


class PeriodActiveUsers:
    _users_list: list[frozenset]
    _accumulation_period: int
    _unique_users_amount: int

    def __init__(self, accumulation_period: int) -> None:
        """
        Инициализирует объект для подсчета числа уникальных пользователей.

        Args:
            accumulation_period: период времени, для которого необходимо подсчитать
                число уникальных пользователей.

        Raises:
            TypeError, если accumulation_period не может быть округлено и использовано
                для получения целого числа.
            ValueError, если после округления accumulation_period - число, меньшее 1.
        """

        if not isinstance(accumulation_period, Real):
            raise TypeError("Accumulation period must be real number")

        if round(accumulation_period) < 1:
            raise ValueError("Accumulation period must be equal or more than 1")

        self._accumulation_period = int(round(accumulation_period))
        self._users_list = list[frozenset]()
        self._unique_users_amount = 0

    def add_active_users_for_curr_day(self, users: Sequence[UUID]) -> None:
        """
        Обновляет метрику на основании данных о посещении ресурса для текущего дня.

        Args:
            users: последовательность UUID пользователей, посетивших ресурс
                в данный день.
        """

        if len(self._users_list) == self._accumulation_period:
            del self._users_list[self._accumulation_period - 1]

        self._users_list.insert(0, frozenset(list(users)))

        unique_users = set()
        for users in self._users_list:
            unique_users |= users
        self._unique_users_amount = len(unique_users)

    @property
    def unique_users_amount(self) -> int:
        """Число уникальных пользователей за последние accumulation_period дней."""
        return self._unique_users_amount

    @property
    def accumulation_period(self) -> int:
        """Период расчета метрики: accumulation_period."""
        return self._accumulation_period
