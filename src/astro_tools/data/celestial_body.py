from dataclasses import dataclass
from .atmospheres import AtmosphereModel

G = 6.67430e-11         # m^3 / kg * s^2

@dataclass(frozen=True)
class CelestialBody:
    name: str
    radius: float
    mass: float
    orbital_period: float
    rotation_period: float | None = None
    soi: float | None = None
    atmosphere: AtmosphereModel | None = None

    @property
    def mu(self) -> float:
        return  self.mass * G