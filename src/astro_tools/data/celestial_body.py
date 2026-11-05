from dataclasses import dataclass
from .atmospheres import AtmosphereModel


@dataclass(frozen=True)
class CelestialBody:
    name: str
    radius: float
    mu: float
    rotation_period: float | None = None
    atmosphere: AtmosphereModel | None = None