from dataclasses import dataclass
from .celestial_body import CelestialBody

@property
def mass(self) -> float:
    G = 6.67430e-11
    return self.mu / G

@dataclass(frozen=True)
class KSPBody(CelestialBody):
    soi: float | None = None
    atmosphere_cutoff_altitude: float | None = None
