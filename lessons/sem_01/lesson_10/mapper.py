from typing import Generator, Callable, Iterable
from circle import circle

def mapper(f: Callable, *args: Iterable, policy: str = "short", fillvalue = None) -> Generator:
    if not isinstance(f, Callable):
        raise TypeError(
           "First given argument should be callable, after – iterable\n\
           Policy - \"short\" or \"long\", fillvalue - any."
        )

    match policy:
        case "short":
            for elem in zip(*args):
                yield f(*elem)

        case "long":
            if isinstance(fillvalue, Iterable):
                fillvalue = list(fillvalue)

            list_of_iterables = [list(iterable) for iterable in [*args]]
            needed_length = max([len(i) for i in list_of_iterables])

            for i in range(len(list_of_iterables)):
                while len(list_of_iterables[i]) < needed_length:
                    if not isinstance(fillvalue, Iterable) or len(fillvalue) != len([*args]):
                        list_of_iterables[i].append(fillvalue)
                    else:
                        list_of_iterables[i].append(fillvalue[i])

            for elem in zip(*list_of_iterables):
                yield f(*elem)

        case _:
            raise ValueError("Parameter 'policy' should be \"short\" or \"long\".")
