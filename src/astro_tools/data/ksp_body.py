from dataclasses import dataclass
from .celestial_body import CelestialBody

@dataclass(frozen=True)
class KSPBody(CelestialBody):
    soi: float | None = None
    atmosphere_cutoff_altitude: float | None = None
