from typing import (
    Callable,
    TypeVar,
)

T = TypeVar("T")


def lru_cache(capacity: int) -> Callable[[T], T]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    arguments:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """
    try:
        capacity = int(round(capacity))
        if capacity < 1:
            raise ValueError("Capacity should be equal or more than 1.")
    except:
        raise TypeError("Capacity should be a number.")

    cache = {}

    def _lru_realise(func):
        def wrapper(*args, **kwargs):
            arguments = (args, tuple(kwargs.items()))
            
            print("ARGUMENTS: ", arguments)
            print("TUPLE OF KEYS: ", tuple(cache.keys()))

            if arguments not in tuple(cache.keys()):
                result = func(*args, **kwargs)

                if len(cache) == capacity:
                    # Удаление первого элемента
                    for k in cache.keys():
                        print('>> DELETING: ', (k, cache[k]))
                        del cache[k]
                        break

                cache[arguments] = result

                print(">> PASTED: ", arguments, " --- RESULTED: ", cache[arguments])

                return result
            copy = cache[arguments]
            del cache[arguments]
            cache[arguments] = copy
            print("------------------FOUNDED IN CACHE---------------------")
            print("CACHE[ARGUMENTS] = ", cache[arguments])
            print("LEN OF CACHE: ", len(cache), " --- CAPACITY: ", capacity)
            print("--------------------------------------------------------")
            return cache[arguments]
        return wrapper
    return _lru_realise

