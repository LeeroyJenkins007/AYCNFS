from .celestial_body import CelestialBody
from .ksp_body import KSPBody
from .atmospheres.exponential import ExponentialAtmosphere
from astro_tools.data.atmospheres.ussa import USSA1976
from astro_tools.data.atmospheres.altitude_conversions import kerbin_to_earth_geopotential

SECONDS_PER_DAY = 86400

EARTH = CelestialBody(
    name="Earth",
    radius=6_371_000,
    mass=5.974e24,
    rotation_period=86164.0905,
    atmosphere=ExponentialAtmosphere(
        surface_density=1.255, 
        scale_height=8500
        )
)

MOON = CelestialBody(
    name="Moon",
    radius=1_737_000,
    mass=73.48e21,
    rotation_period=27.32 * SECONDS_PER_DAY,
    atmosphere=None
)

KERBIN = KSPBody(
    name="Kerbin",
    radius=600_000,
    mass=5.2915158e22,
    rotation_period=21_600,
    atmosphere=USSA1976(altitude_converter=kerbin_to_earth_geopotential),
    soi=84_159_286,
    atmosphere_cutoff_altitude=70_000
)