from dataclasses import dataclass
from .celestial_body import CelestialBody

@dataclass(frozen=True)
class KSPBody(CelestialBody):
    atmosphere_cutoff_altitude: float | None = None
