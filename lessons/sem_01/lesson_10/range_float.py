from numbers import Real
from typing import Generator

def range_float(*, stop: Real, start: Real = 0, step: Real = 1) -> Generator:
    if not all(isinstance(parameter, Real) for parameter in [stop, start, step]):
        raise TypeError("Arguments should be real numbers")

    if (step == 0):
        raise ValueError("Argument 'step' cannot be zero")

    if ((stop-start) * step) < 0:
        return (x for x in []) # Empty Generator

    value = start
    while abs(stop - value) >= abs(step):
        yield value
        value += step
