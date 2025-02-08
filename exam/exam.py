# enumerate создает пару
from typing import Iterable

def enumerate(object: Iterable):
    count = 0
    iterator = iter(object)
    while True:
        try:
            yield (count, next(iterator))
            count += 1
        except StopIteration:
            break

for a, b in enumerate([2, 2, 2, 2, 2, 2]):
    print(a, b)