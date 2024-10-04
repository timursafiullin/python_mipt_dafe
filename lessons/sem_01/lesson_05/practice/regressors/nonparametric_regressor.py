from typing import Sequence, Union
from numbers import Real

from regressors.regressor_abc import RegressorABC


class NonparametricRegressor(RegressorABC):

    NEAREST_LIMIT: int = 1

    _abscissa: list[Real]
    _ordinates: list[Real]
    _h_nearest: int

    def __init__(self, h_nearest: int = 5) -> None:

        self._h_nearest = round(h_nearest)

        # Validate h_nearest input
        if self._h_nearest < self.NEAREST_LIMIT:
            raise ValueError(f"ValueError: {h_nearest} is lower than limit NEAREST_LIMIT = {self.NEAREST_LIMIT}")

        self._abscissa = []
        self._ordinates = []

    def fit(self, abscissa: Sequence[Real], ordinates: Sequence[Real]) -> None:
        
        if len(abscissa) != len(ordinates):
            raise ValueError(f"Shape mismatch: {len(abscissa)} != {len(ordinates)}")

        self._abscissa = list(abscissa)
        self._ordinates = list(ordinates)



    def predict(self, abscissa: Union[Real, Sequence[Real]]) -> list:
        if self._abscissa is None or self._ordinates is None:
            raise RuntimeError("fit must be called first")

        if isinstance(abscissa, Real):
            return [self._get_approximation(abscissa)]

        return [
            self._get_approximation(abscissa_i) for abscissa_i in abscissa
        ]
    
    def _get_approximation(self, abscissa: Real) -> float:
        h_index = min(self._h_nearest, len(self._abscissa) - 1)
        h_nearest=  sorted(self._abscissa, key=lambda x: abs(x - abscissa))[h_index]
        window_size = abs(abscissa - h_nearest)

        weights = self._get_weights(abscissa, window_size)

        numerator = sum(
            map(lambda tup_: tup_[0] * tup_[1], zip(self._ordinates, weights)),
        )
        return numerator / sum(weights)

    def _get_weights(self, abscissa: Real, window_size: Real) -> list[float]:

        weights = []

        # Ability to change Kernel
        def Kernel(z: Real):
            if abs(z) < 1:
                return 0.75*(1 - z**2)
            else:
                return 0
            
        for abscissa_i in self._abscissa:
            kernel_value = abs(abscissa_i - abscissa) / window_size
            weight = Kernel(kernel_value)
            weights.append(weight)
        
        return weights


        


