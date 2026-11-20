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
    semi_major_axis=149_598_023_000,
    orbital_period=365.256363004 * SECONDS_PER_DAY,
    atmosphere=ExponentialAtmosphere(
        surface_density=1.255, 
        scale_height=8500
        )
)

MOON = CelestialBody(
    name="Moon",
    radius=1_737_000,
    mass=73.48e21,
    semi_major_axis=384_399_000,
    rotation_period=27.32 * SECONDS_PER_DAY,
    orbital_period=27.321661 * SECONDS_PER_DAY,
    atmosphere=None
)

KERBIN = KSPBody(
    name="Kerbin",
    radius=600_000,
    mass=5.2915158e22,
    rotation_period=21_600,
    orbital_period=9_203_545,
    semi_major_axis=13_599_840_256,
    atmosphere=USSA1976(altitude_converter=kerbin_to_earth_geopotential),
    soi=84_159_286,
    atmosphere_cutoff_altitude=70_000
)

MUN = KSPBody(
    name="Mun",
    radius=200_000,
    mass=9.7599066e20,
    rotation_period=138_984.38,
    orbital_period=138_984,
    semi_major_axis=12_000_000,
    soi=2_429_559.1
)