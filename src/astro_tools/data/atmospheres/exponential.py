import math

from dataclasses import dataclass

@dataclass(frozen=True)
class ExponentialAtmosphere:

    surface_density: float
    scale_height: float

    def density(self, altitude: float) -> float:
        return self.surface_density * math.exp(
            -altitude / self.scale_height
        )
