from uuid import UUID
from metrics import PeriodActiveUsers

# Тесты

# Что если accumulation_period < 1 или вовсе не число
try:
    bad_arg = PeriodActiveUsers(-2)
    bad_arg = PeriodActiveUsers("vehicale")
    raise AssertionError("accumulation_period < 1 did not pass")
except (ValueError, TypeError):
    print("First test passed")

# Проверка округления accumulation_period
round_test = PeriodActiveUsers(1.3)
assert round_test.accumulation_period == round(
    1.3
), "accumulation_period round not working"
round_test = PeriodActiveUsers(1.6)
assert round_test.accumulation_period == round(
    1.6
), "accumulation_period round not working"
print("Second test passed")

# Нормальная работа алгоритма
period = 3
metrica = PeriodActiveUsers(period)
uuid_list = [l for l in "qwerty1367"]

for i in range(10 + period):
    metrica.add_active_users_for_curr_day(uuid_list[i::])
    if i >= period:
        assert metrica.unique_users_amount == 9 + period - i, "normal algorithm not working"
print("Third test passed")
