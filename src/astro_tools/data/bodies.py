from .celestial_body import CelestialBody
from .ksp_body import KSPBody
from .atmospheres.exponential import ExponentialAtmosphere


EARTH = CelestialBody(
    name="Earth",
    radius=6_371_000,
    mu=3.986004418e14,
    rotation_period=86164.0905,
    atmosphere=ExponentialAtmosphere(
        surface_density=1.255, 
        scale_height=8500
        )
)

KERBIN = KSPBody(
    name="Kerbin",
    radius=600_000,
    mu=3.5316e12,
    rotation_period=21_600,
    atmosphere=ExponentialAtmosphere(
        surface_density=1.225,
        scale_height=8500
    ),
    soi=84_159_286,
    atmosphere_cutoff_altitude=70_000
)