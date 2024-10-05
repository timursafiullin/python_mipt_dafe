from typing import Sequence, Union
from numbers import Real
from numpy import average

from regressors.regressor_abc import RegressorABC


class RegressorLSM(RegressorABC):

    _abscissa: list[Real]
    _ordinates: list[Real]
    _b: Real
    _a: Real

    def __init__(self) -> None:

        self._abscissa = []
        self._ordinates = []
        self._b = 0.0
        self._a = 0.0

    def fit(self, abscissa: Sequence[Real], ordinates: Sequence[Real]) -> None:

        if len(abscissa) != len(ordinates):
            raise ValueError(f"Shape mismatch: {len(abscissa)} != {len(ordinates)}")

        self._abscissa = list(abscissa)
        self._ordinates = list(ordinates)
        
        # Чтобы не считать их каждый раз в _get_approximation()
        # average() из numpy
        x_avg = average(self._abscissa)
        y_avg = average(self._ordinates)
        x_squares_avg = average([x**2 for x in self._abscissa])
        xy_avg = average([x*y for x, y in zip(self._abscissa, self._ordinates)])

        self._a = (xy_avg - (x_avg * y_avg)) / (x_squares_avg - (x_avg ** 2))
        self._b = y_avg - self._a * x_avg

    def predict(self, abscissa: Union[Real, Sequence[Real]]) -> list:

        if self._abscissa is None or self._ordinates is None:
            raise RuntimeError("Call method fit() firstly")

        if isinstance(abscissa, Real):
            return [self._get_approximation(abscissa)]

        return [self._get_approximation(abscissa_i) for abscissa_i in abscissa]

    def _get_approximation(self, abscissa: Real) -> float:
        return self._a * abscissa + self._b

