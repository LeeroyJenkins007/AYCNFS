import math
import numpy as np

from astro_tools.data.bodies import KERBIN
from astro_tools.orbital_mechanics import orbital_velocity

from astro_tools.data.atmospheres import USSA1976

print("Kerbin circular orbital velocity at 70km : ", orbital_velocity(KERBIN, 70_000 + KERBIN.radius), " m/s")

def test_kerbin_orbital_velocity():
    radius = KERBIN.radius + 70_000

    expected = 2295

    result = orbital_velocity(KERBIN, radius)

    assert math.isclose(result, expected)

alts = np.arange(0, 80_000, 1)
temps = [USSA1976.molecular_scale_temperature(alt) for alt in alts]