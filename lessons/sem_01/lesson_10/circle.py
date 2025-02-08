from typing import Generator, Iterable

def circle(object: Iterable) -> Generator:
    if not isinstance(object, Iterable):
        raise TypeError("Iterable object expected")

    if isinstance(object, Generator):
        store = list()
        for thing in object:
            yield thing
            store.append(thing)
    else:
        store = object

    if not store:
        raise ValueError("Input iterable object is empty")

    while True:
        for thing in store:
            yield thing
