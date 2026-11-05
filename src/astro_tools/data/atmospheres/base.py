from typing import Protocol

class AtmosphereModel(Protocol):
    def density(self, altitude: float) -> float:
        ...