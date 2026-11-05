import math

from astro_tools.data.bodies import KERBIN
from astro_tools.orbital_mechanics import orbital_velocity

print("Kerbin circular orbital velocity at 70km : ", orbital_velocity(KERBIN, 70_000 + KERBIN.radius), " m/s")

def test_kerbin_orbital_velocity():
    radius = KERBIN.radius + 70_000

    expected = 2295

    result = orbital_velocity(KERBIN, radius)

    assert math.isclose(result, expected)